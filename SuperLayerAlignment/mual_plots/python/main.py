import align_plots, os

def main(plotter):
    os.chdir("C:\Users\Austin\Desktop\SL_Alignment\mual_plots\Text")
    
    x_var = 'sector'
    y_var = 'phiz_100011'
    yo_var = 'station'
    xo_var = 'wheel'

##    plotter.readFile('res_st1234_dumpfidgttn.txt')
##    plotter.readFile('res_st1234_dumpfidgttn_c1.txt')
    plotter.readFile('res_st1234_data_1110_110011_dumplucaini_01.txt')
    plotter.readFile('sign_conventions_mb.txt', True)
    plotter.applySC()

    print "Showing all plots for 1st file"
    plotter.createCanvas()
    plotter.plot([0], x_var, y_var, xo_var, yo_var)
    #plotter.plot(1, x_var, y_var, xo_var, yo_var)

##    raw_input("Next?")
##
##    print "Showing plots from wheel:[-2..2] station:[1..1]"
##    plotter.createCanvas()
##    plotter.setPlotRange(-2,1,2,1)
##    plotter.plot([0], x_var, y_var, xo_var, yo_var)
##
##    raw_input("Next?")
##
##    print "Showing plots from wheel:[-2..-2] station:[1..4]"
##    plotter.createCanvas()
##    plotter.setPlotRange(-2,1,-2,4)
##    plotter.plot([0], x_var, y_var, xo_var, yo_var)
##
##    raw_input("Next?")
##
##    print "Showing all plots for 2nd file"
##    plotter.createCanvas()
##    plotter.setPlotAll()
##    plotter.plot([1], x_var, y_var, xo_var, yo_var)
    

plotter = align_plots.corrections_plotter()
main(plotter)
