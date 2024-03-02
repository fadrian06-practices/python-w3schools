The precedence order is described in the table below, starting with the highest precedence at the top:

Operator 	                                    Description
--------										-----------
() 	                                            Parentheses 	
** 	                                            Exponentiation 	
+x  -x  ~x 	                                    Unary plus, unary minus, and bitwise NOT 	
*  /  //  % 	                                Multiplication, division, floor division, and modulus 	
+  - 	                                        Addition and subtraction 	
<<  >> 	                                        Bitwise left and right shifts 	
& 	                                            Bitwise AND 	
^ 	                                            Bitwise XOR 	
| 	                                            Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
not 	                                        Logical NOT 	
and 	                                        AND 	
or 	                                            OR

If two operators have the same precedence, the expression is evaluated from left to right.