%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg gtk-qt-engine
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		0.8
Release:		%{?tde_version:%{tde_version}_}3
Summary:		Theme engine using Qt for GTK+ 2.x and Trinity
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/themes/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:  tqt3-dev-tools

BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# GTK2 support
BuildRequires:  pkgconfig(gtk+-2.0)



%description
The GTK-Qt Theme Engine (also known as gtk-qt-engine) is a GTK 2 theme engine
that calls Qt to do the actual drawing. This makes your GTK 2 applications
look almost like real Qt applications and gives you a more unified desktop
experience.

Please note that this package is targeted at Trinity users and therefore provides
a way to configure it from within KControl.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_prefix}/%{_lib}/trinity/kcm_kcmgtk.la
%{tde_prefix}/%{_lib}/trinity/kcm_kcmgtk.so
%{tde_prefix}/share/applications/tde/kcmgtk.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/gtk/

# The following files are outside TDE's directory
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/2.10.0
%dir %{_libdir}/gtk-2.0/2.10.0/engines
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.la
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.so
%dir %{_datadir}/themes
%dir %{_datadir}/themes/Qt
%dir %{_datadir}/themes/Qt/gtk-2.0
%{_datadir}/themes/Qt/gtk-2.0/gtkrc

