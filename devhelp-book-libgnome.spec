Summary:	DevHelp book: libgnome
Summary(pl):	Ksi±¿ka do DevHelpa o libgnome
Name:		devhelp-book-libgnome
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libgnome.tar.gz
# Source0-md5:	add4d75c03465782a3070ea469397e4c
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about libgnome.

%description -l pl
Ksi±¿ka do DevHelpa o libgnome.

%prep
%setup -q -c -n libgnome

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/libgnome,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/libgnome.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libgnome

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
