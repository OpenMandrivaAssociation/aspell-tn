%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0.1-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Tswana
%define languagecode tn
# no locale yet
%define lc_ctype tn_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.0.1.0
Release:       %mkrel 10
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
# no tn locale yet
#Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr %{buildroot}

%makeinstall_std

chmod 644 Copyright README* doc/*

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*


