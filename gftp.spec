#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gftp
Version  : 2.0.19
Release  : 6
URL      : https://www.gftp.org/gftp-2.0.19.tar.gz
Source0  : https://www.gftp.org/gftp-2.0.19.tar.gz
Summary  : Multithreaded FTP client for X Windows
Group    : Development/Tools
License  : GPL-2.0 MIT-enna
Requires: gftp-bin = %{version}-%{release}
Requires: gftp-data = %{version}-%{release}
Requires: gftp-license = %{version}-%{release}
Requires: gftp-locales = %{version}-%{release}
Requires: gftp-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : openssl-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : readline-dev
Patch1: 0001-removed-stropts.h-checking.patch

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk. It
features simultaneous downloads, resuming of interrupted file transfers, file 
transfer queues, downloading of entire directories, ftp proxy support, remote 
directory caching, passive and non-passive file transfers, drag-n-drop support,
bookmarks menu, stop button, and many more features.

%package bin
Summary: bin components for the gftp package.
Group: Binaries
Requires: gftp-data = %{version}-%{release}
Requires: gftp-license = %{version}-%{release}

%description bin
bin components for the gftp package.


%package data
Summary: data components for the gftp package.
Group: Data

%description data
data components for the gftp package.


%package license
Summary: license components for the gftp package.
Group: Default

%description license
license components for the gftp package.


%package locales
Summary: locales components for the gftp package.
Group: Default

%description locales
locales components for the gftp package.


%package man
Summary: man components for the gftp package.
Group: Default

%description man
man components for the gftp package.


%prep
%setup -q -n gftp-2.0.19
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565840047
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static HAVE_GRANTPT --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1565840047
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gftp
cp COPYING %{buildroot}/usr/share/package-licenses/gftp/COPYING
cp debian/copyright %{buildroot}/usr/share/package-licenses/gftp/debian_copyright
cp docs/sample.gftp/COPYING %{buildroot}/usr/share/package-licenses/gftp/docs_sample.gftp_COPYING
cp lib/fsplib/COPYING %{buildroot}/usr/share/package-licenses/gftp/lib_fsplib_COPYING
%make_install
%find_lang gftp

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gftp
/usr/bin/gftp-gtk
/usr/bin/gftp-text

%files data
%defattr(-,root,root,-)
/usr/share/applications/gftp.desktop
/usr/share/gftp/COPYING
/usr/share/gftp/bookmarks
/usr/share/gftp/connect.xpm
/usr/share/gftp/deb.xpm
/usr/share/gftp/diff.xpm
/usr/share/gftp/dir.xpm
/usr/share/gftp/doc.xpm
/usr/share/gftp/dotdot.xpm
/usr/share/gftp/down.xpm
/usr/share/gftp/exe.xpm
/usr/share/gftp/gftp-16x16.png
/usr/share/gftp/gftp-22x22.png
/usr/share/gftp/gftp-24x24.png
/usr/share/gftp/gftp-32x32.png
/usr/share/gftp/gftp-48x48.png
/usr/share/gftp/gftp-logo.xpm
/usr/share/gftp/gftp-scalable.svg
/usr/share/gftp/gftp.xpm
/usr/share/gftp/gftprc
/usr/share/gftp/img.xpm
/usr/share/gftp/left.xpm
/usr/share/gftp/linkdir.xpm
/usr/share/gftp/linkfile.xpm
/usr/share/gftp/man.xpm
/usr/share/gftp/open_dir.xpm
/usr/share/gftp/right.xpm
/usr/share/gftp/rpm.xpm
/usr/share/gftp/sound.xpm
/usr/share/gftp/stop.xpm
/usr/share/gftp/tar.xpm
/usr/share/gftp/txt.xpm
/usr/share/gftp/up.xpm
/usr/share/gftp/world.xpm
/usr/share/pixmaps/gftp.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gftp/COPYING
/usr/share/package-licenses/gftp/debian_copyright
/usr/share/package-licenses/gftp/docs_sample.gftp_COPYING
/usr/share/package-licenses/gftp/lib_fsplib_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gftp.1

%files locales -f gftp.lang
%defattr(-,root,root,-)

