#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Template-Toolkit
Version  : 3.102
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Template-Toolkit-3.102.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Template-Toolkit-3.102.tar.gz
Summary  : 'comprehensive template processing system'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Template-Toolkit-bin = %{version}-%{release}
Requires: perl-Template-Toolkit-man = %{version}-%{release}
Requires: perl-Template-Toolkit-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(AppConfig)
BuildRequires : perl(Test::LeakTrace)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Script          Testing
-----------------------------------------------------------------------------
args.t          Passing positional and named arguments to code/object methods
autoform.t      Autoformat plugin (Template::Plugin::Autoformat)
base.t          Template::Base.pm module
binop.t         Binary operators
block.t         BLOCK definition
capture.t       Capture directive output and assign to a variable
case.t          CASE option to switch case sensitivity
compile1.t      Compile templates to Perl code and save to file
compile2.t      Reload above compiled templates without re-parsing
compile3.t      Ensure that touching source template causes re-compilation
compile4.t      Compiling templates to a COMPILE_DIR
compile5.t      Reload templates from a COMPILE_DIR
config.t        Template::Config factory module
context.t       Template::Context module
datafile.t      Datafile plugin (Template::Plugin::Datafile)
date.t          Date plugin (Template::Plugin::Date)
dbi.t           DBI plugin (Template::Plugin::DBI)
directive.t     Directive layout, chomping, comments, etc.
document.t      Template::Document module
dom.t           XML::DOM plugin (Template::Plugin::XML::DOM)
dumper.t        Data::Dumper plugin (Template::Plugin::Data::Dumper)
error.t         Test that errors are reported back to caller as exceptions
evalperl.t      Evaluation of PERL and RAWPERL blocks
exception.t     Template::Exception module
filter.t        FILTER directive and various filters
foreach.t       FOREACH directive
format.t        Format plugin (Template::Plugin::Format)
include.t       INCLUDE and PROCESS directive
iterator.t      Template::Iterator and Iterator plugin modules
list.t          List definition and access via various methods
macro.t         MACRO directive
object.t        Binding objects to template variables
output.t        OUTPUT_PATH and OUTPUT options
parser.t        Template::Parser module
plugins.t       Template::Plugins provider module (incomplete)
process.t       PRE_PROCESS, PROCESS and POST_PROCESS options
provider.t      Template::Provider module
ref.t           Test the \ reference operator (currently undocumented)
rss.t           XML::RSS plugin (Template::Plugin::XML::RSS)
service.t       Template::Service module
skel.t          Skeleton test file.  Copy and edit to create your own tests.
stash.t         Template::Stash module
stop.t          STOP directive and throwing 'stop' exception
switch.t        SWITCH / CASE directives
table.t         Table plugin (Template::Plugin::Table)
tags.t          TAGS directive
template.t      Template front-end module
text.t          Plain text blocks, ensuring all characters are reproducable
try.t           TRY / THROW / CATCH / FINAL directives
url.t           URL plugin (Template::Plugin::URL)
vars.t          Variable usage and GET / SET / CALL / DEFAULT directives
varsv1.t        As above, using version 1 handling of leading '$'
vmeth.t         Virtual scalar/hash/list methods
while.t         WHILE directive
wrap.t          Wrap plugin (Template::Plugin::Wrap)
wrapper.t       WRAPPER directive
xpath.t         XML::XPath plugin (Template::Plugin::XML::XPath)

%package bin
Summary: bin components for the perl-Template-Toolkit package.
Group: Binaries

%description bin
bin components for the perl-Template-Toolkit package.


%package dev
Summary: dev components for the perl-Template-Toolkit package.
Group: Development
Requires: perl-Template-Toolkit-bin = %{version}-%{release}
Provides: perl-Template-Toolkit-devel = %{version}-%{release}
Requires: perl-Template-Toolkit = %{version}-%{release}

%description dev
dev components for the perl-Template-Toolkit package.


%package man
Summary: man components for the perl-Template-Toolkit package.
Group: Default

%description man
man components for the perl-Template-Toolkit package.


%package perl
Summary: perl components for the perl-Template-Toolkit package.
Group: Default
Requires: perl-Template-Toolkit = %{version}-%{release}

%description perl
perl components for the perl-Template-Toolkit package.


%prep
%setup -q -n Template-Toolkit-3.102
cd %{_builddir}/Template-Toolkit-3.102
pushd ..
cp -a Template-Toolkit-3.102 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tpage
/usr/bin/ttree

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Template.3
/usr/share/man/man3/Template::App::ttree.3
/usr/share/man/man3/Template::Base.3
/usr/share/man/man3/Template::Config.3
/usr/share/man/man3/Template::Constants.3
/usr/share/man/man3/Template::Context.3
/usr/share/man/man3/Template::Directive.3
/usr/share/man/man3/Template::Document.3
/usr/share/man/man3/Template::Exception.3
/usr/share/man/man3/Template::FAQ.3
/usr/share/man/man3/Template::Filters.3
/usr/share/man/man3/Template::Grammar.3
/usr/share/man/man3/Template::Iterator.3
/usr/share/man/man3/Template::Manual.3
/usr/share/man/man3/Template::Manual::Config.3
/usr/share/man/man3/Template::Manual::Credits.3
/usr/share/man/man3/Template::Manual::Directives.3
/usr/share/man/man3/Template::Manual::Filters.3
/usr/share/man/man3/Template::Manual::Internals.3
/usr/share/man/man3/Template::Manual::Intro.3
/usr/share/man/man3/Template::Manual::Plugins.3
/usr/share/man/man3/Template::Manual::Syntax.3
/usr/share/man/man3/Template::Manual::VMethods.3
/usr/share/man/man3/Template::Manual::Variables.3
/usr/share/man/man3/Template::Manual::Views.3
/usr/share/man/man3/Template::Modules.3
/usr/share/man/man3/Template::Namespace::Constants.3
/usr/share/man/man3/Template::Parser.3
/usr/share/man/man3/Template::Plugin.3
/usr/share/man/man3/Template::Plugin::Assert.3
/usr/share/man/man3/Template::Plugin::Datafile.3
/usr/share/man/man3/Template::Plugin::Date.3
/usr/share/man/man3/Template::Plugin::Directory.3
/usr/share/man/man3/Template::Plugin::Dumper.3
/usr/share/man/man3/Template::Plugin::File.3
/usr/share/man/man3/Template::Plugin::Filter.3
/usr/share/man/man3/Template::Plugin::Format.3
/usr/share/man/man3/Template::Plugin::HTML.3
/usr/share/man/man3/Template::Plugin::Image.3
/usr/share/man/man3/Template::Plugin::Iterator.3
/usr/share/man/man3/Template::Plugin::Math.3
/usr/share/man/man3/Template::Plugin::Pod.3
/usr/share/man/man3/Template::Plugin::Procedural.3
/usr/share/man/man3/Template::Plugin::Scalar.3
/usr/share/man/man3/Template::Plugin::String.3
/usr/share/man/man3/Template::Plugin::Table.3
/usr/share/man/man3/Template::Plugin::URL.3
/usr/share/man/man3/Template::Plugin::View.3
/usr/share/man/man3/Template::Plugin::Wrap.3
/usr/share/man/man3/Template::Plugins.3
/usr/share/man/man3/Template::Provider.3
/usr/share/man/man3/Template::Service.3
/usr/share/man/man3/Template::Stash.3
/usr/share/man/man3/Template::Stash::Context.3
/usr/share/man/man3/Template::Stash::XS.3
/usr/share/man/man3/Template::Test.3
/usr/share/man/man3/Template::Toolkit.3
/usr/share/man/man3/Template::Tools.3
/usr/share/man/man3/Template::Tools::tpage.3
/usr/share/man/man3/Template::Tools::ttree.3
/usr/share/man/man3/Template::Tutorial.3
/usr/share/man/man3/Template::Tutorial::Datafile.3
/usr/share/man/man3/Template::Tutorial::Web.3
/usr/share/man/man3/Template::VMethods.3
/usr/share/man/man3/Template::View.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tpage.1
/usr/share/man/man1/ttree.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
