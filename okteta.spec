%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A simple HEX editor for KDE
Name:		okteta
Version:	0.25.0
Release:	1
Epoch:		2
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
%{_datadir}/kxmlgui5/oktetapart
%{_datadir}/kxmlgui5/okteta
%{_bindir}/okteta
%{_bindir}/struct2osd
%{_sysconfdir}/xdg/okteta-structures.knsrc
%{_datadir}/metainfo/org.kde.okteta.appdata.xml
%{_datadir}/config.kcfg/structviewpreferences.kcfg
%{_datadir}/mime/packages/okteta.xml
%{_iconsdir}/*/*/apps/okteta.png
%{_libdir}/qt5/plugins/oktetapart.so

#----------------------------------------------------------------------------

%define kasten3controllers_major 3
%define libkasten3controllers %mklibname kasten3controllers %{kasten3controllers_major}

%package -n %{libkasten3controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2controllers 0} < 1:14.12.0

%description -n %{libkasten3controllers}
Okteta shared library.

%files -n %{libkasten3controllers}
%{_libdir}/libkasten3controllers.so.%{kasten3controllers_major}
%{_libdir}/libkasten3controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten3core_major 3
%define libkasten3core %mklibname kasten3core %{kasten3core_major}

%package -n %{libkasten3core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2core 0} < 1:14.12.0

%description -n %{libkasten3core}
Okteta shared library.

%files -n %{libkasten3core}
%{_libdir}/libkasten3core.so.%{kasten3core_major}
%{_libdir}/libkasten3core.so.0.*

#----------------------------------------------------------------------------

%define kasten3gui_major 3
%define libkasten3gui %mklibname kasten3gui %{kasten3gui_major}

%package -n %{libkasten3gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2gui 0} < 1:14.12.0

%description -n %{libkasten3gui}
Okteta shared library.

%files -n %{libkasten3gui}
%{_libdir}/libkasten3gui.so.%{kasten3gui_major}
%{_libdir}/libkasten3gui.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1controllers_major 1
%define libkasten3okteta1controllers %mklibname kasten3okteta1controllers %{kasten3okteta1controllers_major}

%package -n %{libkasten3okteta1controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1controllers 0} < 1:14.12.0

%description -n %{libkasten3okteta1controllers}
Okteta shared library.

%files -n %{libkasten3okteta1controllers}
%{_libdir}/libkasten3okteta1controllers.so.%{kasten3okteta1controllers_major}
%{_libdir}/libkasten3okteta1controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1core_major 1
%define libkasten3okteta1core %mklibname kasten3okteta1core %{kasten3okteta1core_major}

%package -n %{libkasten3okteta1core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1core 0} < 1:14.12.0

%description -n %{libkasten3okteta1core}
Okteta shared library.

%files -n %{libkasten3okteta1core}
%{_libdir}/libkasten3okteta1core.so.%{kasten3okteta1core_major}
%{_libdir}/libkasten3okteta1core.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1gui_major 1
%define libkasten3okteta1gui %mklibname kasten3okteta1gui %{kasten3okteta1gui_major}

%package -n %{libkasten3okteta1gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1gui 0} < 1:14.12.0

%description -n %{libkasten3okteta1gui}
Okteta shared library.

%files -n %{libkasten3okteta1gui}
%{_libdir}/libkasten3okteta1gui.so.%{kasten3okteta1gui_major}
%{_libdir}/libkasten3okteta1gui.so.0.*

#----------------------------------------------------------------------------

%define okteta2core_major 2
%define libokteta2core %mklibname okteta2core %{okteta2core_major}

%package -n %{libokteta2core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1core 1} < 1:14.12.0

%description -n %{libokteta2core}
Okteta shared library.

%files -n %{libokteta2core}
%{_libdir}/libokteta2core.so.%{okteta2core_major}
%{_libdir}/libokteta2core.so.0.*

#----------------------------------------------------------------------------

%define okteta2gui_major 2
%define libokteta2gui %mklibname okteta2gui %{okteta2gui_major}

%package -n %{libokteta2gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1gui 1} < 1:14.12.0

%description -n %{libokteta2gui}
Okteta shared library.

%files -n %{libokteta2gui}
%{_libdir}/libokteta2gui.so.%{okteta2gui_major}
%{_libdir}/libokteta2gui.so.0.*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Okteta
Group:		Development/KDE and Qt
Requires:	%{libkasten3controllers} = %{EVRD}
Requires:	%{libkasten3core} = %{EVRD}
Requires:	%{libkasten3gui} = %{EVRD}
Requires:	%{libkasten3okteta1controllers} = %{EVRD}
Requires:	%{libkasten3okteta1core} = %{EVRD}
Requires:	%{libkasten3okteta1gui} = %{EVRD}
Requires:	%{libokteta2core} = %{EVRD}
Requires:	%{libokteta2gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications that use Okteta libraries.

%files devel
%{_includedir}/*
%{_libdir}/libkasten3controllers.so
%{_libdir}/libkasten3core.so
%{_libdir}/libkasten3gui.so
%{_libdir}/libkasten3okteta1controllers.so
%{_libdir}/libkasten3okteta1core.so
%{_libdir}/libkasten3okteta1gui.so
%{_libdir}/libokteta2core.so
%{_libdir}/libokteta2gui.so
%{_libdir}/qt5/plugins/designer/oktetawidgets.so
%{_libdir}/cmake/OktetaKastenGui
%{_libdir}/cmake/OktetaKastenCore
%{_libdir}/cmake/OktetaKastenControllers
%{_libdir}/cmake/OktetaGui
%{_libdir}/cmake/OktetaCore
%{_libdir}/cmake/KastenGui
%{_libdir}/cmake/KastenCore
%{_libdir}/cmake/KastenControllers

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
