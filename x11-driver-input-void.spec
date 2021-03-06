Name:		x11-driver-input-void
Version:	1.4.1
Release:	16
Summary:	X.org null input driver
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-void-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.18
BuildRequires:	x11-util-macros >= 1.0.1
Conflicts:	xorg-x11-server < 7.0
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Void is a dummy/null X.org input driver.
It doesn't connect to any physical device, and it never delivers any events.
It functions as both a pointer and keyboard device, and may be used as X
server's core pointer and/or core keyboard.
It's purpose is to allow the X server to operate without a core pointer
and/or core keyboard.

%prep
%setup -qn xf86-input-void-%{version}
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.*
