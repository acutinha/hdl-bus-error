Internal Bus Error:

Author: Akhil Robertson Cutinha

The test.py script is designed to catch the error that occurs in HDL code when an internal bus
is sub-bussed. In HDL only the Input and Output pins are allowed to be subbussed.

Installation:

python -m virtualenv dev 	(create python virtual environment) 
dev/scripts/activate     	(activate it) 
maturin develop 	 	(build parser) 
python test.py 		 	(Run Script) 

The script takes 1 input i.e. the HDL filename as a String. Remember to input the .hdl extention
and make sure that the file is accessible and present in the same directory. One of the sample 
HDL files attached with the code is Mux.hdl, upon passing it to the script, the script parses 
through Mux.hdl and checks for any sub bussing errors. In the example script attached, Mux.hdl 
has 1 internal sub bussing error and therefore, the output will be;

OUTPUT:
Enter the name of the HDL file (along with .hdl): Mux.hdl
Internal bus of "aAndsel" cannot be sub bussed
Bus length : 1
Bus Length used: 3
You are using larger bus than available
Do you want to test another program? [y/n]:

Another HDL file can be checked for sub bussing error by inputing 'y' to the above question
providing the file name followign the rules written above.

Things to Work On:

-The parser cannot read PC chip. It closes the parser when it encounters a the PC chip in
 TrafficController.
	Output:
	{'inputs': [{'end': 0, 'name': 'reset', 'start': 0}],
 	'name': 'TrafficController',
 	'outputs': [{'end': 4, 'name': 'count', 'start': 4},
   	          {'end': 2, 'name': 'light', 'start': 2},
 	            {'end': 2, 'name': 'gr', 'start': 2},
 	            {'end': 0, 'name': 'gree', 'start': 0}],
 	'parts': []}

-The program is designed to work with multiple bit inputs and outputs, however, it would not
 be able to detect sub bussing of pins greater than size 1 because the parser does not map the
 input and output pins bus sizes as of yet. Therefore, that could be worked on specific for the
 program or the parser could be updated to reflect the sizes of the internal (external to the gate)
 pins.
	Eg:
		Mux16(a[0]= pS1,a[1]=pS2, b[0..1]= false, sel= red, out[0..1]= reg1);
	Parser Output:
		{'external': [{'end': 0, 'name': 'pS1', 'start': 0},
                         {'end': 0, 'name': 'pS2', 'start': 0},
                         {'end': 0, 'name': 'false', 'start': 0},
                         {'end': 0, 'name': 'red', 'start': 0},
                         {'end': 0, 'name': 'reg1', 'start': 0}],
            'internal': [{'end': 0, 'name': 'a', 'start': 0},
                         {'end': 1, 'name': 'a', 'start': 1},
                         {'end': 1, 'name': 'b', 'start': 0},
                         {'end': 0, 'name': 'sel', 'start': 0},
                         {'end': 1, 'name': 'out', 'start': 0}],
            'name': 'Mux16'}
 In the above example we can clearly see that the reg1 pin has bus size of 2 while the parser
 shows that it has a bus size of 1 starting at 0 and ending at 0. The bus size of 2 is shown
 in the internal field with name = 'out'.
 Therefore, if the bus size of the internal and external keys are mapped then the program
 would work for all bus sizes. (Personally, I felt rather than having them defined in here,
 having the parser map them would help future projects as well).