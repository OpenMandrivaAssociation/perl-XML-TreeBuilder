%define	modname    XML-TreeBuilder

Name:		perl-%{modname}
Version:	5.4
Release:	1

Summary:	Build a tree of XML::Element objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/XML/XML-TreeBuilder-%{version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Element)
BuildRequires:	perl(HTML::Tagset)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::Catalog)
BuildArch:	noarch

%description
This is just a subclass of HTML::Element. It works basically the same as
HTML::Element, except that tagnames and attribute names aren't forced to
lowercase, as they are in HTML::Element.

the HTML::Element manpage describes everything you can do with this class.

%prep
%autosetup -p1 -n %{modname}-%{version}
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" --skipdeps </dev/null

%build
%make_build

%install
%make_install

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 4.0.0-2mdv2011.0
+ Revision: 657476
- rebuild for updated spec-helper

* Sun Mar 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 4.0.0-1
+ Revision: 642383
- new version

* Mon Jun 14 2010 Jérôme Quelin <jquelin@mandriva.org> 3.90.0-1mdv2011.0
+ Revision: 548037
- import perl-XML-TreeBuilder


* Mon Jun 14 2010 cpan2dist 3.09-1mdv
- initial mdv release, generated with cpan2dist

