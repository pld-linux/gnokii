Summary:	Linux/Unix tool suite for mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzêdzi dla telefonów komórkowych
Name:		gnokii
Version:	0.5.10
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
#Source0:	http://savannah.nongnu.org/download/gnokii/%{name}-%{version}.tar.bz2
Source0:	ftp://urtica.linuxnews.pl/pub/people/pkot/gnokii/%{name}-%{version}.tar.bz2
# Source0-md5:	2c1919774f5948b8d291d32267df70e2
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
for mobile phones.

%description -l pl
Gnokii jest zestawem narzêdzi dla Linuksa/Uniksa, oraz sterownikiem
modemu/faxu dla telefonów komórkowych.

%package X11
Summary:	Graphical Linux/Unix tool suite for mobile phones
Summary(pl):	Zestaw narzêdzi z graficznym interfejsem dla telefonów komórkowych
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Xgnokii jest zestawem narzêdzi z graficznym interfejsem u¿ytkownika
do pracy z telefonami komórkowymi. Pozwalaj± one na edytowanie
spisu telefonów, wysy³anie/czytanie wiadomo¶ci SMS i wiele innych
rzeczy.

%package devel
Summary:	%{name} heades files
Summary(pl):	Pliki nag³ówkowe gnokii
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
gnokii header files.

%description devel -l pl
Pliki nag³ówkowe gnokii.

%prep
%setup -q
%patch0 -p1
#patch1 -p1

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
