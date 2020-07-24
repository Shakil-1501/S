
# Session2 - Object Mutability and Interning

## Objective : To pass the test cases given in test_session2.py

---

### Classes

#### Something

   * It has one attribute called something_new which is initialized through __init__ constructor.There is no method defined in it.
   
  
 #### SomethingNew
 
   * It had two attributes called i whose default value is zero  and something which is of type Something class whose
     default value is None is done through __init__ constructor


    
 ## Functions
 
 ### add_something
  
   * It has got two parameters collection which is of type list of Something object and i which is of type int
   
   * Here we are creating an object of Something class in the first line.
   
   * In the second line we are creating an object of SomethingNew class and assigning it to something_new
   
   * In the third line we  are appending something to collection list
   
 ### reserved_function
 
   * We have used pass keyword so that it can be used in future
   
 ### critical_function
 
   * It is defining collection as list variables 
   
   * We are calling add_something function which was defined above 131072 times
   
   * Once the loop is done , memory can be free using Garbage Collector or once when the session end.
   
   * Instead of wating for Garbage Collector to free up memory we can free the memory while mapping represnting as Weak Reference.
   
 ### clear_memory
 
   *  Return a weak reference to object. The original object can be retrieved by calling the reference object if 
      the referent is still alive; if the referent is no longer alive, calling the reference object will 
      cause None to be returned. 
   
   *  If callback is provided and not None, and the returned weakref object is still alive, 
      the callback will be called when the object is about to be finalized;
      
   *  the weak reference object will be passed as the only parameter to the callback; 
      the referent will no longer be available.
   
 ### compare_strings_old
 
   * Here we have two reference variable a and b which is pointing to a memory location which is storing value of string type
   
   * Here we are suboptimally testing whether two strings are exactly same or not with the help of assignment operator
   
   * After that we are trying to see if we have a particular character in that string or not
   
   * char_list is the list of characters
   
   * Currently the code is suboptimal
   
   * We are also monitoring the time it took to complete the execution
   
 ### compare_strings_new
 
   * Here we have two reference variable a and b and is interned which is pointing to a memory location which is storing value of string type
   
   * sleep method of time module is called to simulate the slow code
   
   * We are doing the interning with the help of sys module.
   
   * Here we are suboptimally testing whether two strings are exactly same or not with the help of assignment operator
   
   *  We are also monitoring the time it took to complete the execution
   
   ## Test cases
   
   *  test clear memory : It checks  whether the difference between the memory usage of last and first element of
                           list is less than 4 otherwise Assertion error.
                           
   *  test_memory_actually_increased : It checks whether the difference between the memory usage of element having peak
                                        memory consumption and the first element of list is greater than 8
                                        
   *  test_performance : It check the performance of two methods in time of execution and it passes once the second functions is greater than or equal to 10.
    
   * test_readme_exists : It checks whether readme file is present or not if fails give "README.md file missing!"
   
   * test_readme_contents : It checks whether words in readme file is greater than or equal to 500 or not.
    
   * test_readme_proper_description:  It checks the quality of Readme if it contains some mentioned words otherwise give assertion error.
    
   * test_readme_file_for_formatting: It check whether the readme file has count has got more than or equal to 10 hash or not.
    
   * test_class_repr(): It checks the special methods repr is present in the class or not
    
   * test_fourspace():  It Returns pass if used four spaces for each level of syntactically 
    
   * test_function_name_had_cap_letter: It checks for capital letter in function name if fails give "You have used Capital letter(s) in your function names" as Assertion error
 
    
   
   ---
   
   Author Info :
   
- Facebook -- [md.shakiluzzaman](https://www.facebook.com/shakil.uzzaman.5/)


  
 
 
 

