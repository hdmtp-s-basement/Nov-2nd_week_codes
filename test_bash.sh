#https://learnxinyminutes.com/docs/bash/

var="Get some"
echo ${var}
echo ${var/some/Go}

Length=7
echo ${var:0:Length}
echo ${var: -5}
echo ${#var}

var2=var
echo ${!var2}

echo ${Foo:-"DefaultValueIfFooIsMissingOrEmpty"}

# Declare an array with 6 elements
array0=(one two three four five six)
# Print first element
echo $array0 # => "one"
# Print first element
echo ${array0[0]} # => "one"
# Print all elements
echo ${array0[@]} # => "one two three four five six"
# Print number of elements
echo ${#array0[@]} # => "6"
# Print number of characters in third element
echo ${#array0[2]} # => "5"
# Print 2 elements starting from forth
echo ${array0[@]:3:2} # => "four five"

# Print all elements. Each of them on new line.
for i in "${array0[@]}"; do
    echo "${i}"
done

# Brace Expansion { }
# Used to generate arbitrary strings
echo {1..10} # => 1 2 3 4 5 6 7 8 9 10
echo {a..z} # => a b c d e f g h i j k l m n o p q r s t u v w x y z
# This will output the range from the start value to the end value

echo "------------------------------"

# Built-in variables:
# There are some useful built-in variables, like
echo "Last program's return value: $?"
echo "Script's PID: $$"
echo "Number of arguments passed to script: $#"
echo "All arguments passed to script: $@"
echo "Script's arguments separated into different variables: $1 $2..."

echo "------------------------------"

# Now that we know how to echo and use variables,
# let's learn some of the other basics of bash!

# Our current directory is available through the command `pwd`.
# `pwd` stands for "print working directory".
# We can also use the built-in variable `$PWD`.
# Observe that the following are equivalent:
echo "I'm in $(pwd)" # execs `pwd` and interpolates output
echo "I'm in $PWD" # interpolates the variable

clear
# Ctrl-L also works for clearing output


# Reading a value from input:
echo "What's your name?"
read Name # Note that we didn't need to declare a new variable
echo Hello, $Name!


# We have the usual if structure:
# use `man test` for more info about conditionals
if [ "$Name" != $USER ]
then
    echo "Your name isn't your username"
else
    echo "Your name is your username"
fi
# True if the value of $Name is not equal to the current user's login username

echo "-------------------------------"

# There is also conditional execution
echo "Always executed" || echo "Only executed if first command fails"
# => Always executed
echo "Always executed" && echo "Only executed if first command does NOT fail"
# => Always executed
# => Only executed if first command does NOT fail

echo "-----------------------------------"

echo $(alias -p)

# There is also the `=~` operator, which tests a string against a Regex pattern:
Email=me@example.com
if [[ "$Email" =~ [a-z]+@[a-z]{2,}\.(com|net|org) ]]
then
    echo "Valid email!"
fi
# Note that =~ only works within double [[ ]] square brackets,
# which are subtly different from single [ ].
# See https://www.gnu.org/software/bash/manual/bashref.html#Conditional-Constructs for more on this.

# Expressions are denoted with the following format:
echo $(( 10 + 5 )) # => 15

echo "----------------------------------------------"

# Unlike other programming languages, bash is a shell so it works in the context
# of a current directory. You can list files and directories in the current
# directory with the ls command:
ls # Lists the files and subdirectories contained in the current directory
echo "----------------------------------------------"
# This command has options that control its execution:
ls -l # Lists every file and directory on a separate line
echo "----------------------------------------------"
ls -t # Sorts the directory contents by last-modified date (descending)
echo "----------------------------------------------"
ls -R # Recursively `ls` this directory and all of its subdirectories
