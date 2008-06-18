Name: x11-driver-input-void
Version: 1.1.1
Release: %mkrel 5
Summary: X.org null input driver
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-void-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
Void is a dummy/null X.org input driver.
It doesn't connect to any physical device, and it never delivers any events.
It functions as both a pointer and keyboard device, and may be used as X
server's core pointer and/or core keyboard.
It's purpose is to allow the X server to operate without a core pointer
and/or core keyboard.

%prep
%setup -q -n xf86-input-void-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/void_drv.la
%{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.*
