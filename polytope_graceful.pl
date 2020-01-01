use application "polytope";

my @files = ("1-1-1", "2-1-1", "3-1-1", "2-2-1", "4-1-1", "3-2-1", "2-2-2", 
"5-1-1", "4-2-1", "3-3-1", "3-2-2", "6-1-1", "5-2-1", "4-3-1", "4-2-2", "3-3-2",
, "7-1-1", "8-1-1");

foreach my $file (@files) {
    open(INPUT, "< ".$file."poly");
    my $A=new Matrix<Rational>(<INPUT>);
    close(INPUT);
    my $p=new Polytope(POINTS=>$A);
    open(my $fh, '>', $file."points"); 
    print $fh $p->N_LATTICE_POINTS;
    close $fh;
    open($fh, '>', $file."facets");
    print $fh $p->FACETS;
    close $fh;
    my $n_graceful_ends = 0;
    open($fh, '<', $file."poly");
    #open my $fh, '<', $filename or die qq{Cannot open "$filename": $!};
    while (sysread $fh, my $buffer, 4096) {
        $n_graceful_ends += ($buffer =~ tr/\n//);
    }
    close $fh;
    open($fh, '>', $file."temp");
    print $fh $p->N_LATTICE_POINTS." ".$n_graceful_ends;
    close $fh;
    open($fh, '>', $file.".ehrhart");
    print $fh $p->EHRHART_POLYNOMIAL_COEFF;
    close $fh;
    tikz($p->VISUAL, File=>$file);
}

