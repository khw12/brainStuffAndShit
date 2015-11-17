from jpype import *
import random


jarLocation = "./infodynamics.jar"

# Start the JVM (add the "-Xmx" option with say 1024M if you get crashes due to not enough memory space)
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=" + jarLocation)


# TODO put down what is the actual data to compute over 
# Generate some random binary data.
#sourceArray = [random.randint(0,1) for r in range(100)]
#destArray = [0] + sourceArray[0:99]
#sourceArray2 = [random.randint(0,1) for r in range(100)]


mi_cal_class = JPackage("infodynamics.measures.continuous.kraskov").MultiInfoCalculatorKraskov2
mi_cal = mi_cal_class(2,1) # TODO http://lizier.me/joseph/software/jidt/javadocs/v1.3/infodynamics/measures/continuous/kraskov/ConditionalMutualInfoCalculatorMultiVariateKraskov2.html



'''
# Create a TE calculator and run it:
teCalcClass = JPackage("infodynamics.measures.discrete").TransferEntropyCalculatorDiscrete
teCalc = teCalcClass(2,1)
teCalc.initialise()
# Since we have simple arrays of ints, we can directly pass these in:
teCalc.addObservations(sourceArray, destArray)
print("For copied source, result should be close to 1 bit : %.4f" % teCalc.computeAverageLocalOfObservations())
teCalc.initialise()
teCalc.addObservations(sourceArray2, destArray)
print("For random source, result should be close to 0 bits: %.4f" % teCalc.computeAverageLocalOfObservations())
'''
shutdownJVM()
