Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzędzi dla telefonów komórkowych Nokia
Name:		gnokii
Version:	0.5.5
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	ftp://ftp.gnokii.org/pub/gnokii/%{name}-%{version}.tar.bz2
# Source0-md5:	8033f9e1e8e1dd1e852db53d44a1df5e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-libtool.patch
URL:		http://www.gnokii.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for Nokia's mobile phones, released under the GPL.

%description -l pl
Gnokii jest zestawem narzędzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefonów komórkowych Nokia, dostępnym na
licencji GPL.

%package X11
Summary:	Graphical Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Zestaw narzędzi z graficznym interfejsem dla telefonów komórkowych Nokia
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for Nokia's mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Gnokii-X11 jest zestawem narzędzi z graficznym interfejsem użytkownika
do pracy z telefonami komórkowymi Nokia. Pozwalają one na edytowanie
spisu telefonów, wysyłanie/czytanie wiadomości SMS i wiele innych
rzeczy.

%package devel
Summary:	%{name} heades files
Summary(pl):	Pliki nagłówkowe gnokii
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
gnokii header files.

%description devel -l pl
Pliki nagłówkowe gnokii.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-security \
	--with-xgnokiidir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/{x,}gnokii} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir},%{_applnkdir}/Utilities}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/{CREDITS,DataCalls-QuickStart,README*,Bugs,FAQ,*.txt,protocol}
%doc Docs/{sample/{gnokiirc,ppp*,ringtone,vCalendar,vCard},gnokii-{ir-howto,IrDA-Linux}}
%doc TODO ChangeLog MAINTAINERS
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_bindir}/todologo
%attr(755,root,root) %{_bindir}/sendsms
%attr(755,root,root) %{_bindir}/ppm2nokia
%attr(755,root,root) %{_sbindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gnokiirc
%attr(755,root,root) %{_libdir}/libgnokii.so.*.*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgnokii
%{_libdir}/xgnokii
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*
%dir %{_datadir}/xgnokii
%{_datadir}/xgnokii/xpm
%{_datadir}/xgnokii/help

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/libgnokii.so
%{_pkgconfigdir}/*.pc
