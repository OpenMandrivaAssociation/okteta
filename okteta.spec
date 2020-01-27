%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A simple HEX editor for KDE
Name:		okteta
Version:	0.26.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	pkgconfig(shared-mime-info)

%description
Okteta is a simple editor for the raw data of files. This type of program
is also called hex editor or binary editor.

%files -f all.lang
%{_datadir}/applications/org.kde.okteta.desktop
%{_datadir}/okteta
%{_bindir}/okteta
%{_bindir}/struct2osd
%{_sysconfdir}/xdg/okteta-structures.knsrc
%{_datadir}/metainfo/org.kde.okteta.appdata.xml
%{_datadir}/config.kcfg/structureviewpreferences.kcfg
%{_datadir}/mime/packages/okteta.xml
%{_iconsdir}/*/*/apps/okteta.png
%{_datadir}/kservices5/oktetapart.desktop
%{_libdir}/qt5/plugins/kf5/parts/oktetapart.so

#----------------------------------------------------------------------------

%define kasten4controllers_major 0
%define libkasten4controllers %mklibname Kasten4Controllers %{kasten4controllers_major}

%package -n %{libkasten4controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2controllers 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3controllers 3} < 3:0.26.2

%description -n %{libkasten4controllers}
Okteta shared library.

%files -n %{libkasten4controllers}
%{_libdir}/libKasten4Controllers.so.%{kasten4controllers_major}*

#----------------------------------------------------------------------------

%define kasten4core_major 0
%define libkasten4core %mklibname Kasten4Core %{kasten4core_major}

%package -n %{libkasten4core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2core 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3core 3} < 3:0.26.2

%description -n %{libkasten4core}
Okteta shared library.

%files -n %{libkasten4core}
%{_libdir}/libKasten4Core.so.%{kasten4core_major}*

#----------------------------------------------------------------------------

%define kasten4gui_major 0
%define libkasten4gui %mklibname Kasten4Gui %{kasten4gui_major}

%package -n %{libkasten4gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2gui 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3gui 3} < 3:0.26.2

%description -n %{libkasten4gui}
Okteta shared library.

%files -n %{libkasten4gui}
%{_libdir}/libKasten4Gui.so.%{kasten4gui_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2controllers_major 0
%define libkasten4okteta2controllers %mklibname Kasten4Okteta2Controllers %{kasten4okteta2controllers_major}

%package -n %{libkasten4okteta2controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1controllers 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3okteta1controllers 1} < 3:0.26.2

%description -n %{libkasten4okteta2controllers}
Okteta shared library.

%files -n %{libkasten4okteta2controllers}
%{_libdir}/libKasten4Okteta2Controllers.so.%{kasten4okteta2controllers_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2core_major 0
%define libkasten4okteta2core %mklibname Kasten4Okteta2Core %{kasten4okteta2core_major}

%package -n %{libkasten4okteta2core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1core 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3okteta1core 1} < 3:0.26.2

%description -n %{libkasten4okteta2core}
Okteta shared library.

%files -n %{libkasten4okteta2core}
%{_libdir}/libKasten4Okteta2Core.so.%{kasten4okteta2core_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2gui_major 0
%define libkasten4okteta2gui %mklibname Kasten4Okteta2Gui %{kasten4okteta2gui_major}

%package -n %{libkasten4okteta2gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1gui 0} < 1:14.12.0
Obsoletes:	%{mklibname kasten3okteta1gui 1} < 3:0.26.2

%description -n %{libkasten4okteta2gui}
Okteta shared library.

%files -n %{libkasten4okteta2gui}
%{_libdir}/libKasten4Okteta2Gui.so.%{kasten4okteta2gui_major}*

#----------------------------------------------------------------------------

%define okteta3core_major 0
%define libokteta3core %mklibname Okteta3Core %{okteta3core_major}

%package -n %{libokteta3core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1core 1} < 1:14.12.0
Obsoletes:	%{mklibname okteta2core 1} < 3:0.26.2

%description -n %{libokteta3core}
Okteta shared library.

%files -n %{libokteta3core}
%{_libdir}/libOkteta3Core.so.%{okteta3core_major}*

#----------------------------------------------------------------------------

%define okteta3gui_major 0
%define libokteta3gui %mklibname Okteta3Gui %{okteta3gui_major}

%package -n %{libokteta3gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1gui 1} < 1:14.12.0
Obsoletes:	%{mklibname okteta2gui 2} < 3:0.26.2

%description -n %{libokteta3gui}
Okteta shared library.

%files -n %{libokteta3gui}
%{_libdir}/libOkteta3Gui.so.%{okteta3gui_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Okteta
Group:		Development/KDE and Qt
Requires:	%{libkasten4controllers} = %{EVRD}
Requires:	%{libkasten4core} = %{EVRD}
Requires:	%{libkasten4gui} = %{EVRD}
Requires:	%{libkasten4okteta2controllers} = %{EVRD}
Requires:	%{libkasten4okteta2core} = %{EVRD}
Requires:	%{libkasten4okteta2gui} = %{EVRD}
Requires:	%{libokteta3core} = %{EVRD}
Requires:	%{libokteta3gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications that use Okteta libraries.

%files devel
%{_includedir}/*
%{_libdir}/libKasten4Controllers.so
%{_libdir}/libKasten4Core.so
%{_libdir}/libKasten4Gui.so
%{_libdir}/libKasten4Okteta2Controllers.so
%{_libdir}/libKasten4Okteta2Core.so
%{_libdir}/libKasten4Okteta2Gui.so
%{_libdir}/libOkteta3Core.so
%{_libdir}/libOkteta3Gui.so
%{_libdir}/qt5/plugins/designer/oktetawidgets.so
%{_libdir}/cmake/OktetaKastenGui
%{_libdir}/cmake/OktetaKastenCore
%{_libdir}/cmake/OktetaKastenControllers
%{_libdir}/cmake/OktetaGui
%{_libdir}/cmake/OktetaCore
%{_libdir}/cmake/KastenGui
%{_libdir}/cmake/KastenCore
%{_libdir}/cmake/KastenControllers
%{_libdir}/pkgconfig/OktetaCore.pc
%{_libdir}/pkgconfig/OktetaGui.pc
%{_libdir}/qt5/mkspecs/modules/qt_OktetaCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_OktetaGui.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkasten
%find_lang liboktetacore
%find_lang liboktetagui
%find_lang liboktetakasten
%find_lang okteta --with-html
%find_lang oktetapart
cat *.lang >all.lang
