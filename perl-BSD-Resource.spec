%include	/usr/lib/rpm/macros.perl
%define		pdir	BSD
%define		pnam	Resource
Summary:	BSD::Resource Perl module
Summary(cs):	Modul BSD::Resource pro Perl
Summary(da):	Perlmodul BSD::Resource
Summary(de):	BSD::Resource Perl Modul
Summary(es):	Módulo de Perl BSD::Resource
Summary(fr):	Module Perl BSD::Resource
Summary(it):	Modulo di Perl BSD::Resource
Summary(ja):	BSD::Resource Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	BSD::Resource ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul BSD::Resource
Summary(pl):	Modu³ Perla BSD::Resource
Summary(pt):	Módulo de Perl BSD::Resource
Summary(pt_BR):	Módulo Perl BSD::Resource
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl BSD::Resource
Summary(sv):	BSD::Resource Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl BSD::Resource
Summary(zh_CN):	BSD::Resource Perl Ä£¿é
Name:		perl-BSD-Resource
Version:	1.15
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BSD::Resource - BSD process resource limit and priority functions.

%description -l pl
BSD::Resource - modu³ zawiera rozszerzon± implementacjê funkcji
ograniczenia zasobów procesów i pierwszeñstwa procesów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/BSD/Resource.pm
%dir %{perl_sitearch}/auto/BSD/Resource
%{perl_sitearch}/auto/BSD/Resource/*.al
%{perl_sitearch}/auto/BSD/Resource/autosplit.ix
%{perl_sitearch}/auto/BSD/Resource/Resource.bs
%attr(755,root,root) %{perl_sitearch}/auto/BSD/Resource/Resource.so
%{_mandir}/man3/*
