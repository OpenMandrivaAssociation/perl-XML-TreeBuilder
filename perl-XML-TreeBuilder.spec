%define upstream_name    XML-TreeBuilder
%define upstream_version 4.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Build a tree of XML::Element objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTML::Element)
BuildRequires: perl(HTML::Tagset)
BuildRequires: perl(XML::Parser)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is just a subclass of HTML::Element. It works basically the same as
HTML::Element, except that tagnames and attribute names aren't forced to
lowercase, as they are in HTML::Element.

the HTML::Element manpage describes everything you can do with this class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


