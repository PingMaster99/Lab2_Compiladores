 (*
* Arithmetic test for Among Us Compiler
* Bool can be added or subtracted with ints
*
*)

class Main {

    -- int
    int_a : Int <- 2;
    int_b : Int <- 5;

    -- bool
    bool_a : Bool <- true;
    bool_b: Bool <- false;

    -- string
    string_a: String <- "Python";
    string_b: String <- "Compilers";

    main() : SELF_TYPE {
	{
	    int_a <- int_a + int_b * bool_a;
            bool_a <- bool_a * bool_b;
            string_a <- string_a * int_a;
            int_b <- int_b / int_a;
            int_a <- int_b - bool_b;
        self;
	}
    };
};