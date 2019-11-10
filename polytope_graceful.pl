use application "polytope";
use strict;
# polymake --script count_lattice_points.perl

my @files = ("1-1-1", "2-1-1", "3-1-1", "2-2-1", "4-1-1", "3-2-1", "2-2-2", 
"5-1-1", "4-2-1", "3-3-1", "3-2-2", "6-1-1", "5-2-1", "4-3-1", "4-2-2", "3-3-2");

foreach my $file (@files) {
    open(INPUT, "< ".$file."poly");
    my $A=new Matrix<Rational>(<INPUT>);
    close(INPUT);
    my $p=new Polytope(POINTS=>$A);
    open(my $fh, '>', $file."points"); 
    print $fh "number vertices: ",$p->N_VERTICES,"\\\\number lattice points: "
    ,$p->N_LATTICE_POINTS,"\\\\";
    close $fh;
    open($fh, '>', $file."facets");
    print $fh $p->FACETS;
    close $fh;
    tikz($p->VISUAL, File=>$file);
}

