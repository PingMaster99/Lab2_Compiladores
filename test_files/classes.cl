class FirstClass {
   integer_1 : Int <- 0;
   value() : Int { integer_1 };
};

class SecondClass inherits FirstClass {

   testFunction(firstNumber : Int) : Int {
      (let test : Int in
	 {
	        -- should always be zero
            test <- firstNumber - firstNumber;
	 }
      )
   };

};

class Main {
   
   unused_declaration : String;
   my_variable : FirstClass;



   main() : Object {
      {

           my_variable <- (new SecondClass);

      }
   };

};
