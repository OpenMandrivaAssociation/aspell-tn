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
Release:       %mkrel 12
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
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-10mdv2011.0
+ Revision: 662874
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-9mdv2011.0
+ Revision: 603467
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-8mdv2010.1
+ Revision: 518968
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-7mdv2010.0
+ Revision: 413110
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1.0-6mdv2009.1
+ Revision: 350124
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1.0-5mdv2009.0
+ Revision: 220455
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1.0.1.0-4mdv2008.1
+ Revision: 182661
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-2mdv2007.0
+ Revision: 123378
- Import aspell-tn

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0.1-0-1mdk
- new realease

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.0-1mdk
- first version

