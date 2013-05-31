library(ggplot2)

theme_set(theme_bw())

save_png <- function(fname, w, h) {
  dev.copy(png, fname, width=w, height=h)
  dev.off()
}

### read in the corrections results data

setwd("C:/Users/khotilov/Downloads")

file_dd0='hw_phiz123.txt'
#file_dd = 'sw_phiz123.txt'
file_dd = 'sw_phiz123fgt.txt'

file_dd0='hw_x13.txt'
file_dd = 'sw_x13fgt.txt'
#file_dd = 'sw_x13fgt_sign.txt'

dd = read.table(file_dd,header=T)
head(dd, n=2)

dd0 = read.table(file_dd0,header=T)
head(dd0, n=2)

dd = merge(dd,dd0)
head(dd, n=2)

### read in the sign conventions and coordinates

sstop= read.table('sign_conventions_mb.txt',header=T, nrows=1)
sstop
classes <- sapply(sstop, class)
classes
classes["label"]="character"
classes
ss = read.table('sign_conventions_mb.txt',header=T, colClasses=classes)
head(ss, n=2)

### combine into a single data frame

d = merge(dd,ss)
d["gdx"] = d["dx"]*d["signx"]
d["gdy"] = d["dy"]*d["signy"]
d["gdphiyx"] = d["dphiyx"]*d["signx"]*d["signz"]
d["gdphizx"] = d["dphizx"]*d["signx"]*d["signy"]
d["gdb"] = d["db"]*d["signx"]*d["signy"]
d["gdai"] = d["dai"]*d["signx"]
d["gdphizsl2"] = d["dphizsl2"]*d["signx"]*d["signy"]
head(d, n=2)




########## in local coordinates

### dphiz between SL1 & 3

qqe = ggplot(dd, aes(hw_db, sw_db)) + 
  stat_abline(intercept=0, slope=1,color=I("grey70")) +
  stat_abline(intercept=0, slope=0,color=I("grey70")) +
  stat_abline(intercept=0, slope=999,color=I("grey70")) + 
  opts(title="both axes: phiz(SL1 WRT ideal) - phiz(SL3 WRT ideal), mrad") +
  coord_equal(ratio = 1)

qqe + geom_point(color="blue") + facet_grid(station~wheel, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dphiz-SL13__grid-st-wh.png", 1100, 710)

qqe + geom_point(color="blue") + facet_grid(station~sector, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dphiz-SL13__grid-st-sec.png",1500,500)

qqe + geom_point(color="blue") + facet_grid(wheel~sector, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dphiz-SL13__grid-wh-sec.png",1500, 600)

#### SL2

qqe = ggplot(dd[dd$station<4,], aes(hw_dphiz2 , sw_dphiz2)) + 
  stat_abline(intercept=0, slope=1,color=I("grey70")) +
  stat_abline(intercept=0, slope=0,color=I("grey70")) +
  stat_abline(intercept=0, slope=999,color=I("grey70")) + 
  opts(title="both axes: dphiz SL2, mrad") +
  coord_equal(ratio = 1)

qqe + geom_point(color="blue") + facet_grid(station~wheel, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dphiz-SL2__grid-st-wh__from-y1.png", 1100, 800)


qqe = ggplot(dd[dd$station<4 & dd$wheel==0,], aes(hw_dphiz2 , sw_dphiz2)) + 
  stat_abline(intercept=0, slope=1,color=I("grey70")) +
  stat_abline(intercept=0, slope=0,color=I("grey70")) +
  stat_abline(intercept=0, slope=999,color=I("grey70")) + 
  opts(title="both axes: dphiz SL2, mrad") +
  coord_equal(ratio = 1)

qqe + geom_point(color="blue") + facet_grid(~station, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dphiz-SL2__grid-st-wh__from-y1-w0.png", 900, 600)


# x13
 

qqe = ggplot(dd, aes(hw_dx13, sw_dx13)) + 
  stat_abline(intercept=0, slope=1,color=I("grey70")) +
  stat_abline(intercept=0, slope=0,color=I("grey70")) +
  stat_abline(intercept=0, slope=999,color=I("grey70")) + 
  opts(title="both axes: x(SL1 WRT ideal) - x(SL3 WRT ideal), mm") +
  coord_equal(ratio = 1)

qqe + geom_point(color="blue") + facet_grid(station~wheel, labeller=label_both) + 
  scale_y_continuous("geometry with track-based corrections") +
  scale_x_continuous("in currfent HW-based geometry")
save_png("swhw_dx-SL13__grid-st-wh.png", 650, 800)
