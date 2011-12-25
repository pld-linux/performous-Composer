Summary:	Composer - song editor for Performous
Name:		performous-Composer
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://downloads.sourceforge.net/performous/Composer-%{version}-source.tar.bz2
# Source0-md5:	d67bee0f50b1f8d35f4f1745fb63484e
Patch0:		%{name}-ffmpeg.patch
Patch1:		%{name}-note_split.patch
URL:		http://performous.org/composer
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	phonon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composer is a song editor for creating (and converting) notes for
music games in various formats. It attempts to make the process easy
by automating as much as possible while providing a simple and
attractive interface to do the remaining manual work.

Key features of Composer include:

    - Song pitch analysis based on the esteemed algorithms from Perfomous.
    - Zoomable interface to quickly get an overview or doing very precise
      timing.
    - Possibility to synthesize the notes to get a feel of their "sound".
    - Import/export in various formats including: SingStar XML
    - UltraStar TXT Frets on Fire MIDI

Composer has a rather distinguished workflow: for example, the lyrics
are imported as a whole and each time you manually put a note in
place, the others automatically adjust to take use of the new
information in providing a better guess of the pitch and timing. In a
sense, you are not actually creating a song, but fixing and tuning the
result of what the computer thinks the notes should be like.

%prep
%setup -qc

%patch0 -p1
%patch1 -p1

%build
mkdir build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.{txt,html}
%attr(755,root,root) %{_bindir}/composer
%{_pixmapsdir}/*
%{_desktopdir}/*
