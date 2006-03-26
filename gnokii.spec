Summary:	Linux/Unix tool suite for mobile phones
Summary(pl):	Linuksowy/uniksowy zestaw narzêdzi dla telefonów komórkowych
Name:		gnokii
Version:	0.6.12
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.gnokii.org/download/gnokii/%{name}-%{version}.tar.bz2
# Source0-md5:	846e03e7cf3581000c9d0141c2950b79
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-smsdlibs.patch
URL:		http://www.gnokii.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.8-2
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0
#BuildRequires:	libical-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	libgnokii = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for mobile phones.

%description -l pl
Gnokii jest zestawem narzêdzi dla Linuksa/Uniksa, oraz sterownikiem
modemu/faksu dla telefonów komórkowych.

%package X11
Summary:	Graphical Linux/Unix tool suite for mobile phones
Summary(pl):	Zestaw narzêdzi z graficznym interfejsem dla telefonów komórkowych
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
Xgnokii is graphical Linux/Unix tool suite for mobile phones. It
allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Xgnokii jest zestawem narzêdzi z graficznym interfejsem u¿ytkownika do
pracy z telefonami komórkowymi. Pozwalaj± one na modyfikowanie spisu
telefonów, wysy³anie/czytanie wiadomo¶ci SMS i wiele innych rzeczy.

%package -n libgnokii
Summary:	A gnokii shared library
Summary(pl):	Biblioteka wspó³dzielona gnokii
Group:		Libraries
Conflicts:	gnokii < 1:0.5.10-0.2

%description -n libgnokii
A gnokii shared library.

%description -n libgnokii -l pl
Biblioteka wspó³dzielona gnokii.

%package -n libgnokii-devel
Summary:	libgnokii heades files
Summary(pl):	Pliki nag³ówkowe biblioteki libgnokii
Group:		Development/Libraries
Requires:	bluez-libs-devel >= 2.8-2
Requires:	libgnokii = %{epoch}:%{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXpm-devel
Obsoletes:	gnokii-devel

%description -n libgnokii-devel
libgnokii header files.

%description -n libgnokii-devel -l pl
Pliki nag³ówkowe biblioteki libgnokii.

%package -n libgnokii-static
Summary:	Static libgnoki library
Summary(pl):	Statyczna biblioteka libgnokii
Group:		Development/Libraries
Requires:	libgnokii-devel = %{epoch}:%{version}-%{release}
Obsoletes:	gnokii-devel

%description -n libgnokii-static
Static version of libgnokii library.

%description -n libgnokii-static -l pl
Statyczna wersja biblioteki libgnokii.

%package smsd
Summary:	Daemon for handling incoming and outgoing SMSes using libgnokii
Summary(pl):	Serwer do zarz±dzania przychodzacymi i wychodzacymi SMS-ami przy u¿yciu gnokii
Group:		Daemons
Requires:	gnokii = %{epoch}:%{version}-%{release}
Obsoletes:	smstools

%description smsd
The SMSD (SMS daemon) program is intended for receiving and sending
SMSes.

%description smsd -l pl
Program SMSD (demon SMS) s³u¿y do odbierania i wysy³ania SMS-ów.

%package smsd-mysql
Summary:	MySQL plugin for gnokii-smsd
Summary(pl):	Wtyczka MySQL dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-mysql
MySQL plugin for gnokii-smsd.

%description smsd-mysql -l pl
Wtyczka MySQL dla gnokii-smsd.

%package smsd-pgsql
Summary:	PostgreSQL plugin for gnokii-smsd
Summary(pl):	Wtyczka PostgreSQL dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-pgsql
PostgreSQL plugin for gnokii-smsd.

%description smsd-pgsql -l pl
Wtyczka PostgreSQL dla gnokii-smsd.

%package smsd-file
Summary:	file plugin for gnokii-smsd
Summary(pl):	Wtyczka obs³ugi plików dla gnokii-smsd
Group:		Daemons
Requires:	gnokii-smsd = %{epoch}:%{version}-%{release}

%description smsd-file
Plain file plugin for gnokii-smsd

%description smsd-file -l pl
Wtyczka obs³ugi plików dla gnokii-smsd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -rf autom4te.cache
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-security \
	--with-xgnokiidir=%{_prefix} \
	%{?debug:--enable-fulldebug}
%{__make}

cd smsd
%{__make}
%{__make} libpq.la
%{__make} libmysql.la
%{__make} libfile.la
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/{x,}gnokii} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install install-docs \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C smsd install \
	DESTDIR=$RPM_BUILD_ROOT

install Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

install -d $RPM_BUILD_ROOT%{_datadir}/xgnokii/xpm
install xgnokii/xpm/* $RPM_BUILD_ROOT%{_datadir}/xgnokii/xpm/

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# do not complain about unpackaged files (we package them with %%doc anyway)
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

# move xgnokii manpage into proper place
mv -f $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}/man1/xgnokii.1x

rm -f $RPM_BUILD_ROOT%{_libdir}/smsd/*.{la,a}

%find_lang %{name}

%clean
#rm -rf $RPM_BUILD_ROOT

%post	-n libgnokii -p /sbin/ldconfig
%postun -n libgnokii -p /sbin/ldconfig

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnokiirc
%{_mandir}/man1/[!x]*
%{_mandir}/man8/gnokiid.*
%{_mandir}/man8/mgnokiidev.*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgnokii
%dir %{_datadir}/xgnokii
%{_libdir}/xgnokii
%{_datadir}/xgnokii/xpm
%{_datadir}/xgnokii/help
%{_desktopdir}/gnokii.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/xgnokii.1x*

%files -n libgnokii
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnokii.so.*.*

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

%files -n gnokii-smsd
%defattr(644,root,root,755)
%doc smsd/ChangeLog smsd/README smsd/README.MySQL smsd/README.Tru64 smsd/action smsd/*.sql
%attr(755,root,root) %{_sbindir}/smsd
%attr(755,root,root) %{_libdir}/smsd/*.so
%{_mandir}/man8/smsd.*

%files -n gnokii-smsd-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libmysql.so

%files -n gnokii-smsd-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libpq.so

%files -n gnokii-smsd-file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smsd/libfile.so
