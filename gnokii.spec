Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzêdzi dla telefonów komórkowych Nokia
Name:		gnokii
Version:	0.4.3
Release:	4
License:	GPL v2+
Group:		Applications/Communications
Source0:	ftp://ftp.gnokii.org/pub/gnokii/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-ac_gettext_fixes.patch
URL:		http://www.gnokii.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xprefix	/usr/X11R6
%define		_xbindir	%{_xprefix}/bin
%define		_xlibdir	%{_xprefix}/lib
%define		_xdatadir	%{_xprefix}/share

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for Nokia's mobile phones, released under the GPL.

%description -l pl
Gnokii jest zestawem narzêdzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefonów komórkowych Nokia, dostêpnym na
licencji GPL.

%package X11
Summary:	Graphical Linux/Unix tool suite for Nokia mobile phones.
Summary(pl):	Zestaw narzêdzi z graficznym interfejsem dla telefonów komórkowych Nokia.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for Nokia's mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Gnokii-X11 jest zestawem narzêdzi z graficznym interfejsem u¿ytkownika
do pracy z telefonami komórkowymi Nokia. Pozwalaj± one na edytowanie
spisu telefonów, wysy³anie/czytanie wiadomo¶ci SMS i wiele innych
rzeczy.

%prep
%setup -q
%patch0 -p1
%patch1

%build
rm -f missing
%{__autoheader}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-security \
	--with-xgnokiidir=%{_xprefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/gnokii} \
	$RPM_BUILD_ROOT{%{_xbindir},%{_xlibdir}/xgnokii} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir},%{_applnkdir}/Utilities}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

install common/libgnokii.so $RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/{CREDITS,DataCalls-QuickStart,README*,Bugs,FAQ,*.txt,protocol}
%doc Docs/{sample/{gnokiirc,ppp*,ringtone,vCalendar,vCard},gnokii-{ir-howto,IrDA-Linux}}
%doc TODO ChangeLog MAINTAINERS
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_bindir}/todologo
%attr(755,root,root) %{_sbindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%attr(755,root,root) %{_libdir}/libgnokii.so
%config(noreplace) %{_sysconfdir}/gnokiirc

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/xgnokii
%{_xlibdir}/xgnokii
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*
%dir %{_xdatadir}/xgnokii
%{_xdatadir}/xgnokii/xpm
%{_xdatadir}/xgnokii/help
