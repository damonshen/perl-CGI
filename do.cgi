#!/usr/bin/perl -w
use CGI;
my $cgi = new CGI;
my $nick = $cgi->param('nick');
my $color = $cgi->param('color');

#print "Content-type: text/html\n\n"; # HTTP header
print $cgi->header("text/html");
print "Hello World!<br />"; # any valid HTML
print "$nick likes $color!\n"; # any valid HTML
