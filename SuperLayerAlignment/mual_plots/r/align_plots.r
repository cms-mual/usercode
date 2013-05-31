library(ggplot2)

theme_set(theme_bw())

save_png <- function(fname) {
  dev.copy(png, fname, width=1400, height=800)
  dev.off()
}

### read in the corrections results data

#setwd("C:/Users/khotilov/Downloads")
#setwd("C:\Users\khotilov\Work\alignment\mual_plots\mual_plots_20111201")
setwd("C:\\Users\\Austin\\Desktop\\mual_plots_20111201\\Text")

file_dd0 = 'res_st1234_dump.txt'
file_dd0 = 'res_st1234_dumpfid.txt'
file_dd0  = 'res_st1234_dumpfidg.txt'
file_dd0  = 'res_st1234_dumpfidgt.txt'
file_dd0  = 'res_st1234_dumpfidgtt.txt'
file_dd0  = 'res_st1234_dumpfidgttn.txt'
file_dd0  = 'res_st1234_dumpfidgttn_c1.txt'
file_dd0  = 'res_st1234_dumpfid_corphiz13.txt'
file_dd0  = 'res_st1234_dumpfidgt_corphiz13.txt'

file_dd  = 'res_st1234_dumpfid.txt'
file_dd  = 'res_st1234_dumpfidg.txt'
file_dd  = 'res_st1234_dumpfidgt.txt'
file_dd  = 'res_st1234_dumpfidgtt.txt'
file_dd  = 'res_st1234_dumpfidgttn.txt'
file_dd  = 'res_st1234_dumpfidgttn_c1.txt'
file_dd  = 'res_st1234_dumpfidgttn_c2.txt'
file_dd  = 'res_st1234_dumpfid_corphiz13.txt'
file_dd  = 'res_st1234_dumpfidgt_corphiz13.txt'

ddtop= read.table(file_dd,header=T, nrows=1)
ddtop
classes <- sapply(ddtop, class)
classes["label"]="character"
classes
dd = read.table(file_dd,header=T, colClasses=classes)
head(dd, n=2)


ddtop= read.table(file_dd0,header=T, nrows=1)
ddtop
classes <- sapply(ddtop, class)
classes["label"]="character"
classes
dd0 = read.table(file_dd0,header=T, colClasses=classes)
head(dd0, n=2)

### read in the sign conventions and coordinates

sstop= read.table('sign_conventions_mb.txt',header=T, nrows=1)
sstop
classes <- sapply(sstop, class)
classes
classes["label"]="character"
classes
ss = read.table('sign_conventions_mb.txt',header=T, colClasses=classes)
head(ss, n=2)

### combine into a single data frame and append global values

d = merge(dd,ss)
d["gx_100000"] = d["x_100000"]*d["signx"]
d["gx_100001"] = d["x_100001"]*d["signx"]
d["gx_100011"] = d["x_100011"]*d["signx"]
d["gx_100111"] = d["x_100111"]*d["signx"]
d["gx_101000"] = d["x_101000"]*d["signx"]
d["gx_111000"] = d["x_111000"]*d["signx"]
d["gy_100000"] = d["y_100000"]*d["signy"]
d["gy_010001"] = d["y_010001"]*d["signy"]
d["gy_010011"] = d["y_010011"]*d["signy"]
d["gy_010111"] = d["y_010111"]*d["signy"]
d["gy_011000"] = d["y_011000"]*d["signy"]
d["gy_111000"] = d["y_111000"]*d["signy"]
d["gz_101000"] = d["z_101000"]*d["signz"]
d["gz_011000"] = d["z_011000"]*d["signz"]
d["gz_111000"] = d["z_111000"]*d["signz"]
d["gphix_100111"] = d["phix_100111"]*d["signy"]*d["signz"]
d["gphix_010111"] = d["phix_010111"]*d["signy"]*d["signz"]
d["gphiy_100011"] = d["phiy_100011"]*d["signx"]*d["signz"]
d["gphiy_000011"] = d["phiy_000011"]*d["signx"]*d["signz"]
d["gphiy_100111"] = d["phiy_100111"]*d["signx"]*d["signz"]
d["gphiy_010011"] = d["phiy_010011"]*d["signx"]*d["signz"]
d["gphiy_010111"] = d["phiy_010111"]*d["signx"]*d["signz"]
d["gphiz_100011"] = d["phiz_100011"]*d["signx"]*d["signy"]
d["gphiz_010001"] = d["phiz_010001"]*d["signx"]*d["signy"]
d["gphiz_000011"] = d["phiz_000011"]*d["signx"]*d["signy"]
d["gphiz_100111"] = d["phiz_100111"]*d["signx"]*d["signy"]
d["gphiz_010011"] = d["phiz_010011"]*d["signx"]*d["signy"]
d["gphiz_010111"] = d["phiz_010111"]*d["signx"]*d["signy"]
d["gdb"] = d["db"]*d["signx"]*d["signy"]
d["gdai"] = d["dai"]*d["signx"]
d["gdphizsl2"] = d["dphizsl2"]*d["signx"]*d["signy"]
head(d, n=2)

d0 = merge(dd0,ss)
d0["gx_100000"] = d0["x_100000"]*d0["signx"]
d0["gx_100001"] = d0["x_100001"]*d0["signx"]
d0["gx_100011"] = d0["x_100011"]*d0["signx"]
d0["gx_100111"] = d0["x_100111"]*d0["signx"]
d0["gx_101000"] = d0["x_101000"]*d0["signx"]
d0["gx_111000"] = d0["x_111000"]*d0["signx"]
d0["gy_100000"] = d0["y_100000"]*d0["signy"]
d0["gy_010001"] = d0["y_010001"]*d0["signy"]
d0["gy_010011"] = d0["y_010011"]*d0["signy"]
d0["gy_010111"] = d0["y_010111"]*d0["signy"]
d0["gy_011000"] = d0["y_011000"]*d0["signy"]
d0["gy_111000"] = d0["y_111000"]*d0["signy"]
d0["gz_101000"] = d0["z_101000"]*d0["signz"]
d0["gz_011000"] = d0["z_011000"]*d0["signz"]
d0["gz_111000"] = d0["z_111000"]*d0["signz"]
d0["gphix_100111"] = d0["phix_100111"]*d0["signy"]*d0["signz"]
d0["gphix_010111"] = d0["phix_010111"]*d0["signy"]*d0["signz"]
d0["gphiy_100011"] = d0["phiy_100011"]*d0["signx"]*d0["signz"]
d0["gphiy_000011"] = d0["phiy_000011"]*d0["signx"]*d0["signz"]
d0["gphiy_100111"] = d0["phiy_100111"]*d0["signx"]*d0["signz"]
d0["gphiy_010011"] = d0["phiy_010011"]*d0["signx"]*d0["signz"]
d0["gphiy_010111"] = d0["phiy_010111"]*d0["signx"]*d0["signz"]
d0["gphiz_100011"] = d0["phiz_100011"]*d0["signx"]*d0["signy"]
d0["gphiz_010001"] = d0["phiz_010001"]*d0["signx"]*d0["signy"]
d0["gphiz_000011"] = d0["phiz_000011"]*d0["signx"]*d0["signy"]
d0["gphiz_100111"] = d0["phiz_100111"]*d0["signx"]*d0["signy"]
d0["gphiz_010011"] = d0["phiz_010011"]*d0["signx"]*d0["signy"]
d0["gphiz_010111"] = d0["phiz_010111"]*d0["signx"]*d0["signy"]
d0["gdb"] = d0["db"]*d0["signx"]*d0["signy"]
d0["gdai"] = d0["dai"]*d0["signx"]
d0["gdphizsl2"] = d0["dphizsl2"]*d0["signx"]*d0["signy"]
head(d0, n=2)


########## common graphic elements

line00 <- stat_abline(intercept=0, slope=0, color=I("grey70"))
facet_st_wh <- facet_grid(station~wheel, labeller=label_both)
facet_st_sec <- facet_grid(station~sector, labeller=label_both)
facet_wh_sec <- facet_grid(wheel~sector, labeller=label_both)



########## in global coordinates

### dphiz between SL1 & 3

ggplot(d, aes(phi, gdb, ymin=gdb-edb, ymax=gdb+edb)) +
  ylab("dphiz' between SL1 - SL3, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphiz-SL13_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gdb, ymin=gdb-edb, ymax=gdb+edb)) +
  ylab("dphiz' between SL1 - SL3, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")
save_png("gdphiz-SL13_vs_phi__grid-st-wh__cor-vs-not.png")
#save_png("gdphiz-SL13_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphiz-SL13_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d, aes(sector, gdb, ymin=gdb-edb, ymax=gdb+edb)) +
  ylab("dphiz' between SL1 - SL3, mrad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL13_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gdb, ymin=gdb-edb, ymax=gdb+edb)) +
  ylab("dphiz' between SL1 - SL3, mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL13_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gdb, ymin=gdb-edb, ymax=gdb+edb)) +
  ylab("dphiz' between SL1 - SL3, mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL13_vs_st__grid-wh-sec.png")


### dai SL13


ggplot(d, aes(dai)) +
  xlab("edx' shift between SL1 - SL3, mm") + line00 + facet_st_wh +
  geom_histogram(color="blue")

ggplot(d, aes(phi, gdai, ymin=gdai-edai, ymax=gdai+edai)) +
  ylab("dx' shift between SL1 - SL3, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdx-SL13_vs_phi__grid-st-wh.png")

ggplot(d[d$edai<0.5,], aes(phi, gdai, ymin=gdai-edai, ymax=gdai+edai)) +
  ylab("dx' shift between SL1 - SL3, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$edai<0.5,],  fatten=1, width = 0.25, color="red")
save_png("gdx-SL13_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdx-SL13_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d, aes(sector, gdai, ymin=gdai-edai, ymax=gdai+edai)) +
  ylab("dx' shift between SL1 - SL3, mm") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdx-SL13_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gdai, ymin=gdai-edai, ymax=gdai+edai)) +
  ylab("dx' shift between SL1 - SL3, mm") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdx-SL13_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gdai, ymin=gdai-edai, ymax=gdai+edai)) +
  ylab("dx' shift between SL1 - SL3, mm") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdx-SL13_vs_st__grid-wh-sec.png")


### dphiz SL2

 
ggplot(d[d$station<4,], aes(phi, gdphizsl2, ymin=gdphizsl2-edphizsl2, ymax=gdphizsl2+edphizsl2)) +
  ylab("dphiz' of SL2 relative to SL13, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphiz-SL2_vs_phi__grid-st-wh.png")

ggplot(d[d$station<4,], aes(phi, gdphizsl2, ymin=gdphizsl2-edphizsl2, ymax=gdphizsl2+edphizsl2)) +
  ylab("dphiz' of SL2 relative to SL13, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$station<4,],  fatten=1, width = 0.25, color="red")
save_png("gdphiz-SL2_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphiz-SL2_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(edphizsl2)) +
  xlab("edphiz' of SL2, mrad") + line00 + facet_st_wh +
  geom_histogram(color="blue")

ggplot(d[d$station<4,], aes(sector, gdphizsl2, ymin=gdphizsl2-edphizsl2, ymax=gdphizsl2+edphizsl2)) +
  ylab("dphiz' of SL2 relative to SL13, mrad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL2_vs_sec__grid-st-wh.png")

ggplot(d[d$station<4,], aes(wheel, gdphizsl2, ymin=gdphizsl2-edphizsl2, ymax=gdphizsl2+edphizsl2)) +
  ylab("dphiz' of SL2 relative to SL13, mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL2_vs_wh__grid-st-sec.png")

ggplot(d[d$station<4,], aes(station, gdphizsl2, ymin=gdphizsl2-edphizsl2, ymax=gdphizsl2+edphizsl2)) +
  ylab("dphiz' of SL2 relative to SL13, mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz-SL2_vs_st__grid-wh-sec.png")



### dphiz

#ggplot(d[d$station<4,], aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011)) +
#ggplot(d[d$station<4,], aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
#ggplot(d, aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
ggplot(d, aes(phi, gphiz_000011, ymin=gphiz_000011-ephiz_000011, ymax=gphiz_000011+ephiz_000011)) +
  ylab("dphiz' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,fatten=1, width = 0.3, color="red") 
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiz_100111, ymin=gphiz_100111-ephiz_100111, ymax=gphiz_100111+ephiz_100111))
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiz_010111, ymin=gphiz_010111-ephiz_010111, ymax=gphiz_010111+ephiz_010111))
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011))
  #geom_crossbar(data=d0[d0$station<4,],  fatten=1, width = 0.25, color="red")

ggplot(d, aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphiz_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")
save_png("gdphiz_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphiz_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011)) +
  ylab("dphiz' of SL2, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,fatten=1, width = 0.35, color="red")
ggplot(d[d$station<4,], aes(phi, gphiz_010001, ymin=gphiz_010001-ephiz_010001, ymax=gphiz_010001+ephiz_010001)) +
  ylab("dphiz' of SL2, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") + 
  geom_crossbar(fatten=1, width = 0.30, color="red", aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011)) +
  geom_crossbar(fatten=1, width = 0.25, color="green", aes(phi, gphiz_010111, ymin=gphiz_010111-ephiz_010111, ymax=gphiz_010111+ephiz_010111))
save_png("gdphiz_vs_phi__grid-st-wh__from_y-1-11-111.png")

ggplot(d[d$station<4,], aes(ephiz_010011)) +
  xlab("edphiz' of SL2, mrad") + line00 + facet_st_wh +
  geom_histogram(color="blue") +
  geom_histogram(color="red", aes(edphizsl2))

ggplot(d[d$station<4,], aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011)) +
  ylab("dphiz' of SL2, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$station<4,],  fatten=1, width = 0.25, color="red")
save_png("gdphiz_vs_phi__SL2__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphiz_vs_phi__SL2__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011))
save_png("gdphiz_vs_phi__grid-st__from-x-vs-y.png")

ggplot(d[d$station<4 & abs(d$wheel)<2,], aes(phi, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiz_010011, ymin=gphiz_010011-ephiz_010011, ymax=gphiz_010011+ephiz_010011))
save_png("gdphiz_vs_phi__grid-st__from-x-vs-y__wh-101.png")


ggplot(d, aes(sector, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gphiz_100011, ymin=gphiz_100011-ephiz_100011, ymax=gphiz_100011+ephiz_100011)) +
  ylab("dphiz' of chamber, mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiz_vs_st__grid-wh-sec.png")


### dphiy

#ggplot(d[d$station<4,], aes(phi, gphiy_010011, ymin=gphiy_010011-ephiy_010011, ymax=gphiy_010011+ephiy_010011)) +
#ggplot(d[d$station<4,], aes(phi, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
#ggplot(d, aes(phi, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  #ylab("dphiy' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  #geom_crossbar(fatten=1, width = 0.35, color="blue")
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiy_100111, ymin=gphiy_100111-ephiy_100111, ymax=gphiy_100111+ephiy_100111))
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiy_010111, ymin=gphiy_010111-ephiy_010111, ymax=gphiy_010111+ephiy_010111))
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiy_010011, ymin=gphiy_010011-ephiy_010011, ymax=gphiy_010011+ephiy_010011))
  #geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")

ggplot(d, aes(phi, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphiy_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")
save_png("gdphiy_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphiy_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(phi, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiy_010011, ymin=gphiy_010011-ephiy_010011, ymax=gphiy_010011+ephiy_010011))
  #geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphiy_000011, ymin=gphiy_000011-ephiy_000011, ymax=gphiy_000011+ephiy_000011))
save_png("gdphiy_vs_phi__grid-st__from-x-vs-y.png")

ggplot(d, aes(sector, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiy_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiy_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gphiy_100011, ymin=gphiy_100011-ephiy_100011, ymax=gphiy_100011+ephiy_100011)) +
  ylab("dphiy' of chamber, mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphiy_vs_st__grid-wh-sec.png")


### dphix

ggplot(d, aes(phi, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphix_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")
save_png("gdphix_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdphix_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(phi, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(fatten=1, width = 0.25, color="red", aes(phi, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111))
save_png("gdphix_vs_phi__grid-st__from-x-vs-y.png")

ggplot(d[d$station<4,], aes(phi, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111)) +
  ylab("dphix' of chamber (from y residuals), mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphix_vs_phi__grid-st__from-y.png")

ggplot(d[d$station<4,], aes(phi, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111)) +
  ylab("dphix' of chamber (from y residuals), mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$station<4,],fatten=1, width = 0.25, color="red")

ggplot(d, aes(sector, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphix_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphix_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gphix_100111, ymin=gphix_100111-ephix_100111, ymax=gphix_100111+ephix_100111)) +
  ylab("dphix' of chamber, mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphix_vs_st__grid-wh-sec.png")


ggplot(d[d$station<4,], aes(ephix_010111)) +
  xlab("dphix error (from y residuals), mrad") + line00 + facet_st_wh +
  geom_histogram(color="blue", binwidth = 0.05)
save_png("gdphix_error__grid-st__from-y.png")

ggplot(d[d$station<4,], aes(phi, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111)) +
  ylab("dphix' of chamber (from y residuals), mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue")
save_png("gdphix_vs_phi__grid-st-wh__from-y.png")

ggplot(d[d$station<4,], aes(wheel, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111)) +
  ylab("dphix' of chamber (from y residuals), mrad") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphix_vs_wh__grid-st-sec__from-y.png")

ggplot(d[d$station<4,], aes(station, gphix_010111, ymin=gphix_010111-ephix_010111, ymax=gphix_010111+ephix_010111)) +
  ylab("dphix' of chamber (from y residuals), mrad") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdphix_vs_st__grid-wh-sec__from-y.png")


### dx

ggplot(d, aes(phi, gx_100011, ymin=gx_100011-ex_100011, ymax=gx_100011+ex_100011)) +
  ylab("dx' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue")
save_png("gdx_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gx_100011, ymin=gx_100011-ex_100011, ymax=gx_100011+ex_100011)) +
  ylab("dx' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.25, color="red")
save_png("gdx_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdx_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d, aes(sector, gx_100011, ymin=gx_100011-ex_100011, ymax=gx_100011+ex_100011)) +
  ylab("dx' of chamber, mm") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue")
save_png("gdx_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gx_100011, ymin=gx_100011-ex_100011, ymax=gx_100011+ex_100011)) +
  ylab("dx' of chamber, mm") + line00 + facet_st_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue")
save_png("gdx_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gx_100011, ymin=gx_100011-ex_100011, ymax=gx_100011+ex_100011)) +
  ylab("dx' of chamber, mm") + line00 + facet_wh_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue")
save_png("gdx_vs_st__grid-wh-sec.png")

ggplot(d, aes(phi, gx_100011/r*1000, ymin=(gx_100011-ex_100011)/r*1000, ymax=(gx_100011+ex_100011)/r*1000)) +
  ylab("global dphiz of chamber, mrad") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue")
save_png("dglobalphiz_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, gx_100011/r*1000, ymin=(gx_100011-ex_100011)/r*1000, ymax=(gx_100011+ex_100011)/r*1000)) +
  ylab("global dphiz of chamber, mrad") + line00 + facet_st_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue")
save_png("dglobalphiz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gx_100011/r*1000, ymin=(gx_100011-ex_100011)/r*1000, ymax=(gx_100011+ex_100011)/r*1000)) +
  ylab("global dphiz of chamber, mrad") + line00 + facet_wh_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue")
save_png("dglobalphiz_vs_st__grid-wh-sec.png")


### dy

ggplot(d[d$station<4,], aes(phi, gy_010001, ymin=gy_010001-ey_010001, ymax=gy_010001+ey_010001)) +
  ylab("dy' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") 
  #geom_crossbar(data=d0[d0$station<4,], fatten=1, width = 0.25, color="red")
save_png("gdy_vs_phi__grid-st-wh.png")

ggplot(d[d$station<4,], aes(phi, gy_010001, ymin=gy_010001-ey_010001, ymax=gy_010001+ey_010001)) +
  ylab("dy' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$station<4,], fatten=1, width = 0.25, color="red")
save_png("gdy_vs_phi__grid-st-wh__tsos4-vs-0.png")
#save_png("gdy_vs_phi__grid-st-wh__fid-vs-nofid.png")

ggplot(d[d$station<4,], aes(sector, gy_010001, ymin=gy_010001-ey_010001, ymax=gy_010001+ey_010001)) +
  ylab("dy' of chamber, mm") + line00 + facet_st_wh +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdy_vs_sec__grid-st-wh.png")

ggplot(d[d$station<4,], aes(wheel, gy_010001, ymin=gy_010001-ey_010001, ymax=gy_010001+ey_010001)) +
  ylab("dy' of chamber, mm") + line00 + facet_st_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdy_vs_wh__grid-st-sec.png")

ggplot(d[d$station<4,], aes(station, gy_010001, ymin=gy_010001-ey_010001, ymax=gy_010001+ey_010001)) +
  ylab("dy' of chamber, mm") + line00 + facet_wh_sec +
  geom_crossbar(fatten=1, width = 0.75, color="blue")
save_png("gdy_vs_st__grid-wh-sec.png")


### dz

ggplot(d, aes(ez_111000)) +
  xlab("edz' of chamber, mm") + line00 + facet_st_wh +
  geom_histogram(color="blue")

ggplot(d, aes(phi, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000)) +
  ylab("dz' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0,  fatten=1, width = 0.30, color="red", aes(phi, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000))
ggplot(d[d$station<4,], aes(phi, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000)) +
  ylab("dz' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d0[d0$station<4,],  fatten=1, width = 0.30, color="red", aes(phi, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000))
#save_png("gdz_vs_phi__grid-st-wh.png")

ggplot(d, aes(phi, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000)) +
  ylab("dz' of chamber, mm") + xlab("global phiz, rad") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.30, color="red", aes(phi, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000)) +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.25, color="green", aes(phi, gz_111000, ymin=gz_111000-ez_111000, ymax=gz_111000+ez_111000))
save_png("gdz_vs_phi__grid-st-wh.png")

ggplot(d, aes(sector, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000)) +
  ylab("dz' of chamber, mm") + line00 + facet_st_wh +
  geom_crossbar(data=d,  fatten=1, width = 0.35, color="blue") +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.30, color="red", aes(sector, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000)) +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.25, color="green", aes(sector, gz_111000, ymin=gz_111000-ez_111000, ymax=gz_111000+ez_111000))
save_png("gdz_vs_sec__grid-st-wh.png")

ggplot(d, aes(wheel, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000)) +
  ylab("dz' of chamber, mm") + line00 + facet_st_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue") +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.65, color="red", aes(wheel, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000)) +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.55, color="green", aes(wheel, gz_111000, ymin=gz_111000-ez_111000, ymax=gz_111000+ez_111000))
save_png("gdz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, gz_101000, ymin=gz_101000-ez_101000, ymax=gz_101000+ez_101000)) +
  ylab("dz' of chamber, mm") + line00 + facet_wh_sec +
  geom_crossbar(data=d,  fatten=1, width = 0.75, color="blue") +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.65, color="red", aes(station, gz_011000, ymin=gz_011000-ez_011000, ymax=gz_011000+ez_011000)) +
  geom_crossbar(data=d[d$station<4,],  fatten=1, width = 0.55, color="green", aes(station, gz_111000, ymin=gz_111000-ez_111000, ymax=gz_111000+ez_111000))
save_png("gdz_vs_st__grid-wh-sec.png")



########## other stuff

qplot(ephiz_100011,ephiy_100011,data=d, facets=~station, color=sector, alpha=I(0.5), size=wheel+3) + scale_colour_gradientn(colour = rainbow(7)) 
dev.copy(png, "errors-correl__edphiyx-vs-edphizx__grid-station.png", width=900, height=800)
dev.off()

qplot(ex_100011,ey_010011,data=d, facets=~station, color=sector, alpha=I(0.5), size=wheel+3) + scale_colour_gradientn(colour = rainbow(7)) 
dev.copy(png, "errors-correl__edy-vs-edx__grid-station.png", width=900, height=800)
dev.off()

qplot(ephiz_100011, edb, data=d, facets=~station, color=sector, alpha=I(0.5), size=wheel+3) + scale_colour_gradientn(colour = rainbow(7))


qplot(ex_100011, data=d, facets=station~wheel)
save_png("error_dx__grid-st-wh.png")

qplot(ey_010011, data=d[d$station<4,], facets=station~wheel)
save_png("error_dy__grid-st-wh.png")


qplot(ephix_100111, data=d, facets=station~wheel)
save_png("error_dphix__grid-st-wh.png")

qplot(ephix_010111, data=d[d$station<4,], facets=station~wheel)
save_png("error_dphix__grid-st-wh__from-y.png")


qplot(ephiy_100011, data=d, facets=station~wheel)
save_png("error_dphiy__grid-st-wh.png")

qplot(ephiy_010011, data=d[d$station<4,], facets=station~wheel)
save_png("error_dphiy__grid-st-wh__from-y.png")


qplot(ephiz_100011, data=d, facets=station~wheel)
save_png("error_dphiz__grid-st-wh.png")

qplot(ephiz_010011, data=d[d$station<4,], facets=station~wheel)
save_png("error_dphiz__grid-st-wh__from-y.png")


qplot(edb, data=d, facets=station~wheel)
save_png("error_dphiz-SL13__grid-st-wh.png")

qplot(edai, data=d, facets=station~wheel)
save_png("error_dx-SL13__grid-st-wh.png")

qplot(edphizsl2, data=d[d$station<4,], facets=station~wheel)
save_png("error_dphiz-SL2__grid-st-wh.png")



plotmatrix((d[d$station<4,])[c("dx","dy","dphiyx","dphizx","db","dai","dphizsl2")])


plotmatrix((d[d$station<4,])[c("edx","edy","edphiyx","edphizx","edb","edai","edphizsl2")])
dev.copy(png, "errors-correl__stations-1-3.png", width=900, height=800)
dev.off()

plotmatrix((d[d$station==1,])[c("edx","edy","edphiyx","edphizx","edb","edai","edphizsl2")])
dev.copy(png, "errors-correl__station-1.png", width=900, height=800)
dev.off()

plotmatrix((d[d$station==2,])[c("edx","edy","edphiyx","edphizx","edb","edai","edphizsl2")])
dev.copy(png, "errors-correl__station-2.png", width=900, height=800)
dev.off()

plotmatrix((d[d$station==3,])[c("edx","edy","edphiyx","edphizx","edb","edai","edphizsl2")])
dev.copy(png, "errors-correl__station-3.png", width=900, height=800)
dev.off()

plotmatrix((d[d$station==4,])[c("edx","edphiyx","edphizx","edb","edai")])
dev.copy(png, "errors-correl__station-4.png", width=900, height=800)
dev.off()



