# TODO: - Work on kaplan
#	- Backport .desktop and icon files for Kaplan from recent CVS
#	- Correct Russian descriptions (for those who understand russian, it is
#	  clear that H (N) is written in lowercase instead uppercase
#	- Recheck dependencies

%define         _ver		1.0.1

Summary:	Personal Information Management (PIM) for KDE
Summary(ko.UTF-8):   K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl.UTF-8):   Program zarządzający informacjami osobistymi (PIM) dla KDE
Summary(ru.UTF-8):   Персональный планировщик (PIM) для KDE
Summary(uk.UTF-8):   Персональный планувальник (PIM) для KDE
Name:		kdepim-kroupware
Version:	%{_ver}
Release:	2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	http://www.erfrakon.de/projects/kolab/download/kde-kolab-client-%{version}/src/%{name}-%{version}.tar.bz2
#Source0-MD5:	72709aaeac03f4deecbc0692ccd65e74
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	perl-base
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	zlib-devel
Requires:	kdelibs >= 3.1.1
Provides:	kdepim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	korganizer
Obsoletes:	kdepim

%define		_prefix		/usr
%define         _htmldir        /usr/share/doc/kde/HTML

%define         no_install_post_chrpath         1

%description
kdepim-kroupware is a collection of Personal Information Management
(PIM) tools for the K Desktop Enviromnent (KDE).

%description -l pl.UTF-8
kdepim-kroupware jest jest zestawem aplikacji PIM dla K Desktop
Enviromnent (KDE).

%description -l ru.UTF-8
kdepim-kroupware - это набор утилит для управления персональной
информацией для K Desktop Enviromnent (KDE).

%description -l uk.UTF-8
kdepim-kroupware - це набір утиліт для керування персональною
информацією для K Desktop Enviromnent (KDE).

%package devel
Summary:	Development files for kdepim-kroupware
Summary(pl.UTF-8):   Pliki nagłówkowe do kdepim-kroupware
Summary(uk.UTF-8):   Файли розробки для kdepim-kroupware
Summary(ru.UTF-8):   Файлы разработки для kdepim-kroupware
Group:		X11/Development/Libraries
Provides:	kdepim-devel
Obsoletes:	kdepim-devel

%description devel
This package contains header files needed if you wish to build
applications based on kdepim-kroupware.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
opartych na kdepim-kroupware.

%description devel -l uk.UTF-8
Цей пакет містить файли заголовків необхідні для побудови програм,
базованих на kdepim-kroupware.

%description devel -l ru.UTF-8
Этот пакет содержит файлы заголовков необходимые для построения
программ, основанных на kdepim-kroupware.

%package kaddressbook
Summary:	Address Book
Summary(pl.UTF-8):   Książka adresowa
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kaddressbook
Address Book

%description kaddressbook -l pl.UTF-8
Książka adresowa

%package kalarm
Summary:	Alarm
Summary(pl.UTF-8):   Alarm
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	kdepim-kalarm
Obsoletes:	kdepim-kalarm

%description kalarm
Reminder Message Scheduler

%description kalarm -l pl.UTF-8
Nastawianie przypominania o zdarzeniach

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl.UTF-8):   Program do komunikacji między PC a tel. komórkowym.
Group:		X11/Applications
Provides:	kdepim-kandy
Obsoletes:	kdepim-cellphone
Obsoletes:	kdepim-kandy

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl.UTF-8
Kandy umożliwia dostęp do telefonu komórkowego i pozwala na
synchronizację danych z telefonu z danymi na PC.

%package kaplan
Summary:	An integrated PIM application
Summary(pl.UTF-8):   Zintegrowany PIM
Group:		X11/Applications
Requires:	kdenetwork-kroupware-kmail >= %{version}
Requires:	kdepim-kroupware-knotes = %{version}-%{release}
Requires:	kdepim-kroupware-kaddressbook = %{version}-%{release}
Requires:	kdepim-kroupware-korganizer = %{version}-%{release}
Provides:	kdepim-kaplan
Obsoletes:	kdepim-kaplan

%description kaplan
Kaplan is a PIM application, whcih integrates the knotes, kmail,
korganizer, kaddressbook parts.

%description kaplan -l pl.UTF-8
Kaplan jest aplikacją PIM integrującą funkcjonalność knotes, kmail,
korganizer i kaddressbook.

%package karm
Summary:	Personal timetracker
Summary(pl.UTF-8):   Osobisty czasomierz
Group:		X11/Applications
Provides:	kdepim-karm
Obsoletes:	kdepim-karm

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl.UTF-8
KArm (nazwa pochodzi od słowa "praca" w języku punjambi) śledzi czas
spędzony na różnych zajęciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunków wielu klientom.

%package kgantt
Summary:	A library to display and manage Gantt diagrams
Summary(pl.UTF-8):   Biblioteka do rysowania diagramów Gantta zarządzania nimi
Group:		X11/Libraries
Provides:	kdepim-kgantt
Obsoletes:	kdepim-kgantt

%description kgantt
A library to display and manage Gantt diagrams.

%description kgantt -l pl.UTF-8
Biblioteka do rysowania diagramów Gantta zarządzania nimi.

%package knotes
Summary:	Yellow cards
Summary(pl.UTF-8):   Żółte karteczki
Group:		X11/Applications
Provides:	kdepim-knotes
Obsoletes:	kdepim-knotes

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl.UTF-8
KNotes pozwala umieszczać na desktopie notatki z opcją wysyłania.
Dodatkowo, aby móc służyć za przypominajkę, KNotes może wysyłać pocztę
i drukować notatki, a także przyjmować przeciąganie nawet ze zdalnych
komputerów.

%package konsolekalendar
Summary:	A command line ICard tool
Summary(pl.UTF-8):   Narzędzie dostępu do plików kalendarza z linii poleceń
Group:		Applications
Provides:	kdepim-konsolekalendar
Obsoletes:	kdepim-konsolekalendar

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl.UTF-8
Narzędzie dostępu do plików kalendarza z linii poleceń.

%package korganizer
Summary:	A complete calendar and scheduling progra
Summary(pl.UTF-8):   Kalendarz wraz z harmonogramem zadań
Group:		X11/Applications
Provides:	kdepim-korganizer
Obsoletes:	kdepim-korganizer

%description korganizer
A complete calendar and scheduling program, which supports information
interchange with other calendar applications through the industry
standard vCalendar file format.

%description korganizer -l pl.UTF-8
Kalendarz wraz z harmonogramem zadań (KOrganizer), który wspiera
wymianę informacji z innymi tego typu aplikacjami poprzez standard
przemysłowy (vCalendar).

%description korganizer -l ru.UTF-8
полнофункциональная программа календаря и персонального планировщика
(KOrganizer поддерживает обмен информацией с другими программами
такого рода через стандартный формат файла vCalendar)

%description korganizer -l uk.UTF-8
повнофункціональна програма календара та персонального
планувальника (KOrganizer підтримує обмін информацією з іншими
програмами такого роду через стандартний формат файлу vCalendar)

%package kpilot
Summary:	A sync tool for palmtops
Summary(pl.UTF-8):   Narzędzie do synchronizacji z palmtopami
Group:		X11/Applications
Requires:	pilot-link
Provides:	kdepim-kpilot
Obsoletes:	kdepim-pilot
Obsoletes:	kpilot
Obsoletes:	kdepim-kpilot

%description kpilot
Synchronization tool for 3Com Palm Pilots and compatible devices.

%description kpilot -l pl.UTF-8
Narzędzie do synchronizacji z 3Com Palm Pilotem i zgodnymi
urządzeniami.

%description kpilot -l ru.UTF-8
утилита для синхронизации с 3com Palm Pilots и совместимыми
с ними устройствами,

%description kpilot -l uk.UTF-8
утиліта для синхронізації з 3com Palm Pilots та сумісними з
ними пристроями.

%package ksync
Summary:	A library for syncing stuff
Summary(pl.UTF-8):   Biblioteka do synchronizacji rzeczy
Group:		X11/Libraries
Provides:	kdepim-ksync
Obsoletes:	kdepim-ksync

%description ksync
libksync is a generic library for syncing collections of data entries
like calenders, bookmarks, contacts, mail folders etc.

%description ksync -l pl.UTF-8
libksync jest standardową biblioteką do synchronizacji zbiorów danych
jak np. kalendarze, zakładki, kontakty, foldery pocztowe itp.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--disable-final

%{__make}

#cd kaplan
#%%{__make}
#cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd kaplan
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
cd ..

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Applications/*,Office/PIMs}
mv $ALD/Utilities/{More/*,.}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*
%{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*
%{_libdir}/kde3/kfile_vcf.la
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so.*
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_libdir}/kde3/kabc_imap.la
%attr(755,root,root) %{_libdir}/kde3/kabc_imap.so
%{_datadir}/apps/kabc/plugins/imap.desktop
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/webcal.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/kde3/*conduit.so

%files kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde3/libkaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_applnkdir}/Utilities/kaddressbook.desktop
%{_pixmapsdir}/*/*/*/kaddressbook.png
%{_datadir}/services/kaddressbook_service.desktop

%files kalarm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/korgac
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart
%{_applnkdir}/.hidden/*
%{_applnkdir}/Office/PIMs/kalarm.desktop
%{_applnkdir}/Utilities/kalarm.desktop
%{_pixmapsdir}/[!l]*/*/*/kalarm.png

%files kandy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_applnkdir}/Utilities/kandy.desktop

%files karm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_applnkdir}/Utilities/karm.desktop
%{_pixmapsdir}/*/*/*/karm.png

%files kaplan
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaplan
%{_libdir}/kde3/libkp*plugin.la
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.so
%{_libdir}/libkpinterfaces*.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*
%{_datadir}/apps/kaplan
%{_datadir}/apps/kp*plugin
%{_datadir}/services/kp*plugin.*
%{_datadir}/servicetypes/kaplanplugin.desktop
%{_applnkdir}/Office/PIMs/Kaplan.desktop
%{_pixmapsdir}/*/*/*/kaplan.png

%files kgantt
%defattr(644,root,root,755)
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*
%{_datadir}/apps/kgantt

%files knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_applnkdir}/Utilities/knotes.desktop
%{_pixmapsdir}/*/*/*/knotes.png

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar

%files korganizer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ical2vcal
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*
#%{_libdir}/libkorg_*.la
#%attr(755,root,root) %{_libdir}/libkorg_*.so
%{_applnkdir}/Office/PIMs/korganizer.desktop
%{_pixmapsdir}/*/*/*/korganizer*.png
%{_libdir}/kde3/*kabc*
/usr/X11R6/share/apps/korganizer/*

%files kpilot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*
%{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so*
%{_datadir}/apps/kpilot
%{_datadir}/services/expense-conduit.desktop
%{_datadir}/services/abbrowser_conduit.desktop
%{_datadir}/services/knotes-conduit.desktop
%{_datadir}/services/null-conduit.desktop
%{_datadir}/services/popmail-conduit.desktop
%{_datadir}/services/time_conduit.desktop
%{_datadir}/services/todo-conduit.desktop
%{_datadir}/services/vcal-conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_applnkdir}/Utilities/kpilot*.desktop
%{_pixmapsdir}/[!l]*/*/*/kpilot*.png

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*
%{_datadir}/apps/ksync
