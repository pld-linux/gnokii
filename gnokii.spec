#
# TODO:
#	- conditional build: X11, smsd, security, and static subpackage
#
# Conditional build:
%bcond_without	bluetooth	# build without bluetooth support
%bcond_without	ical		# build without iCalendar support
%bcond_without	irda		# build without IrDA support
%bcond_without	usb		# build without USB support (for DKU2 cables)
%bcond_without	pcsc		# build without PC/SC Lite support (for Smart Card readers)
%bcond_without	x11		# build without x11

Summary:	Linux/Unix tool suite for mobile phones
Summary(pl.UTF-8):	Linuksowy/uniksowy zestaw narzędzi dla telefonów komórkowych
Name:		gnokii
Version:	0.6.31
Release:	8
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.gnokii.org/download/gnokii/%{name}-%{version}.tar.bz2
# Source0-md5:	d9627f4a1152d3ea7806df4532850d5f
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.smsd.config
Source4:	%{name}.smsd.init
Patch0:		%{name}-pld.patch
Patch1:		no-inline.patch
Patch2:		%{name}-gcc7.patch
Patch3:		%{name}-codeset.patch
URL:		http://www.gnokii.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_bluetooth:BuildRequires:	bluez-libs-devel >= 2.8-2}
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	intltool
%{?with_ical:BuildRequires:	libical-devel}
BuildRequires:	libtool
%{?with_usb:BuildRequires:	libusb-compat-devel}
BuildRequires:	mysql-devel
%{?with_pcsc:BuildRequires:	pcsc-lite-devel}
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	libgnokii = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for mobile phones.

%description -l pl.UTF-8
Gnokii jest zestawem narzędzi dla Linuksa/Uniksa, oraz sterownikiem
modemu/faksu dla telefonów komórkowych.

%package X11
Summary:	Graphical Linux/Unix tool suite for mobile phones
Summary(pl.UTF-8):	Zestaw narzędzi z graficznym interfejsem dla telefonów komórkowych
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
Xgnokii is graphical Linux/Unix tool suite for mobile phones. It
allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl.UTF-8
Xgnokii jest zestawem narzędzi z graficznym interfejsem użytkownika do
pracy z telefonami komórkowymi. Pozwalają one na modyfikowanie spisu
telefonów, wysyłanie/czytanie wiadomości SMS i wiele innych rzeczy.

%package -n libgnokii
Summary:	A gnokii shared library
Summary(pl.UTF-8):	Biblioteka współdzielona gnokii
Group:		Libraries
Conflicts:	gnokii < 1:0.5.10-0.2

%description -n libgnokii
A gnokii shared library.

%description -n libgnokii -l pl.UTF-8
Biblioteka współdzielona gnokii.

%package -n libgnokii-devel
Summary:	libgnokii heades files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgnokii
Group:		Development/Libraries
Requires:	bluez-libs-devel >= 2.8-2
Requires:	libgnokii = %{epoch}:%{version}-%{release}
Requires:	libusb-compat-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXpm-devel
Obsoletes:	gnokii-devel

%description -n libgnokii-devel
libgnokii header files.

%description -n libgnokii-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgnokii.

%package -n libgnokii-static
Summary:	Static libgnoki library
Summary(pl.UTF-8):	Statyczna biblioteka libgnokii
Group:		Development/Libraries
Requires:	libgnokii-devel = %{epoch}:%{version}-%{release}
Obsoletes:	gnokii-devel

%description -n libgnokii-static
Static version of libgnokii library.

%description -n libgnokii-static -l pl.UTF-8
Statyczna wersja biblioteki libgnokii.

%package smsd
Summary:	Daemon for handling incoming and outgoing SMSes using libgnokii
Summary(pl.UTF-8):	Serwer do zarządzania przychodzacymi i wychodzacymi SMS-ami przy użyciu gnokii
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	gnokii = %{epoch}:%{version}-%{release}
Requires:	rc-scripts
Obsoletes:	smstools

%description smsd
The SMSD (SMS daemon) program is intended for receiving and sending
SMSes.

%description smsd -l pl.UTF-8
Program SMSD (demon SMS) służy do odbierania i wysyłania SMS-ów.

%package smsd-mysql
Summary:	MySQL plugin for gnokii-smsd
Summary(pl.UTF-8):	Wtyczka MySQL dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-mysql
MySQL plugin for gnokii-smsd.

%description smsd-mysql -l pl.UTF-8
Wtyczka MySQL dla gnokii-smsd.

%package smsd-pgsql
Summary:	PostgreSQL plugin for gnokii-smsd
Summary(pl.UTF-8):	Wtyczka PostgreSQL dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-pgsql
PostgreSQL plugin for gnokii-smsd.

%description smsd-pgsql -l pl.UTF-8
Wtyczka PostgreSQL dla gnokii-smsd.

%package smsd-sqlite
Summary:	SQLite plugin for gnokii-smsd
Summary(pl.UTF-8):	Wtyczka SQLite dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-sqlite
SQLite plugin for gnokii-smsd.

%description smsd-sqlite -l pl.UTF-8
Wtyczka SQLite dla gnokii-smsd.

%package smsd-file
Summary:	file plugin for gnokii-smsd
Summary(pl.UTF-8):	Wtyczka obsługi plików dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-file
Plain file plugin for gnokii-smsd

%description smsd-file -l pl.UTF-8
Wtyczka obsługi plików dla gnokii-smsd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-security \
	%{!?with_x11:--with-xgnokiidir=%{_prefix}} \
	%{!?with_ical:--disable-libical} \
	%{!?with_usb:--disable-libusb} \
	%{!?with_irda:--disable-irda} \
	%{!?with_bluetooth:--disable-bluetooth} \
	--enable-smsd \
	%{?debug:--enable-fulldebug} \
	%{!?with_pcsc:--disable-libpcsclite}
#	%{!?debug:--disable-debug} \
#	%{!?debug:--disable-xdebug} \
#	%{!?debug:--disable-rlpdebug} \

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d,logrotate.d} \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/{x,}gnokii} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir},%{_desktopdir},%{_var}/log/{smsd,archive/smsd}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C xgnokii install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

install -d $RPM_BUILD_ROOT%{_datadir}/xgnokii/xpm
cp -p xgnokii/xpm/* $RPM_BUILD_ROOT%{_datadir}/xgnokii/xpm

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/smsd
install -p %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/smsd

# do not complain about unpackaged files (we package them with %doc anyway)
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/smsd/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgnokii -p /sbin/ldconfig
%postun -n libgnokii -p /sbin/ldconfig

%post smsd
/sbin/chkconfig --add smsd
%service smsd restart "smsd daemon"

%preun smsd
if [ "$1" = "0" ]; then
	%service smsd stop
	/sbin/chkconfig --del smsd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/{CREDITS,DataCalls-QuickStart,KNOWN_BUGS,README*,Bugs,FAQ,*.txt,protocol}
%doc Docs/{sample,gnokii-{hackers-howto,ir-howto,IrDA-Linux},gnokii.nol} utils/gnapplet.sis
%doc TODO ChangeLog MAINTAINERS
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_bindir}/sendsms
%attr(755,root,root) %{_bindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnokiirc
%{_mandir}/man1/[!x]*
%{_mandir}/man8/gnokiid.*
%{_mandir}/man8/mgnokiidev.*

%files X11
%defattr(644,root,root,755)
%doc xgnokii/{ChangeLog,README.vcard}
%attr(755,root,root) %{_bindir}/xgnokii
%dir %{_datadir}/xgnokii
%{_libdir}/xgnokii
%{_datadir}/xgnokii/xpm
%{_desktopdir}/gnokii.desktop
%{_desktopdir}/xgnokii.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/xgnokii.1x*

%files -n libgnokii
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnokii.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnokii.so.?

%files -n libgnokii-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnokii.so
%{_libdir}/libgnokii.la
%{_includedir}/*.h
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files -n libgnokii-static
%defattr(644,root,root,755)
%{_libdir}/libgnokii.a

%files smsd
%defattr(644,root,root,755)
%doc smsd/ChangeLog smsd/README smsd/README.MySQL smsd/README.Tru64 smsd/action smsd/*.sql
%attr(755,root,root) %{_bindir}/smsd
%dir %{_libdir}/smsd
%{_mandir}/man8/smsd.*
%attr(754,root,root) /etc/rc.d/init.d/smsd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/smsd
%attr(2750,root,logs) %dir /var/log/smsd
%attr(2750,root,logs) %dir /var/log/archive/smsd

%files smsd-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libsmsd_mysql.so

%files smsd-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libsmsd_pq.so

%files smsd-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libsmsd_sqlite.so

%files smsd-file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libsmsd_file.so
