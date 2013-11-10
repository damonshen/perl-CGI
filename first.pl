#!/use/bin/perl
use CGI;

my $cgi = new CGI;
print $cgi->header("text/html");
print "oh yeah baby\n";  
