Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzędzi dla telefonów komórkowych Nokia
Name:		gnokii
Version:	0.4.3
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.gnokii.org/pub/gnokii/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-ac_gettext_fixes.patch
URL:		http://www.gnokii.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
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
Gnokii jest zestawem narzędzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefonów komórkowych Nokia, dostępnym na
licencji GPL.

%package X11
Summary:	Graphical Linux/Unix tool suite for Nokia mobile phones.
Summary(pl):	Zestaw narzędzi z graficznym interfejsem dla telefonów komórkowych Nokia.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for Nokia's mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Gnokii-X11 jest zestawem narzędzi z graficznym interfejsem użytkownika
do pracy z telefonami komórkowymi Nokia. Pozwalają one na edytowanie
spisu telefonów, wysyłanie/czytanie wiadomości SMS i wiele innych
rzeczy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
aclocal
%{__autoconf}
automake -a -c || :
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
%doc Docs/{CREDITS,DataCalls-QuickStart,README{,-{3810,6110}}}
%doc Docs/{sample/gnokiirc,gnokii-ir-howto} TODO
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
