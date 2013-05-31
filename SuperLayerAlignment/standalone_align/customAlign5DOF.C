{
#include <iomanip>

gROOT->SetBatch(1);

//int wh = 0, st = 4, sec = 5;
//TString res_fname="res.txt";
//TString fname = "../data_1110_110011_dumpfid_corphiz13_01.root";
//TString fname = "data_1110_110011_dumpfidtt_01.root";

gSystem->Load("libFit.so");

cout<<endl<<"Starting 1000_100011: "<<endl;
MuonResiduals5DOFFitter fitter(MuonResidualsFitter::kPureGaussian, 1, MuonResidualsFitter::k1000, false);
tt = fitter.readNtuple(fname.Data(), wh, st, sec);
fitter.fix(MuonResiduals5DOFFitter::kAlignZ);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fit();
double dx, dphiyx, dphizx, edx, edphiyx, edphizx;
dx = fitter.value(MuonResiduals5DOFFitter::kAlignX)*10;
edx = fitter.errorerror(MuonResiduals5DOFFitter::kAlignX)*10;
dphiyx = fitter.value(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
edphiyx = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
dphizx = fitter.value(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
edphizx = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
cout<<endl<<"1000_100011: "<<dx<<" +- "<<edx<<"  "<<dphiyx<<" +- "<<edphiyx<<"  "<<dphizx<<" +- "<<edphizx<<endl<<endl;


cout<<endl<<"Starting 1000_100111: "<<endl;
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX,0);
fitter.fit();
double dx_100111, edx_100111, dphixx_100111, edphixx_100111, dphiyx_100111, edphiyx_100111, dphizx_100111, edphizx_100111;
dx_100111 = fitter.value(MuonResiduals5DOFFitter::kAlignX)*10;
edx_100111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignX)*10;
dphixx_100111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiX)*1000;
edphixx_100111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiX)*1000;
dphiyx_100111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
edphiyx_100111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
dphizx_100111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
edphizx_100111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
cout<<"1000_100111: "<<dx_100111<<" +- "<<edx_100111<<"  "<<dphixx_100111<<" +- "<<edphixx_100111<<"  "<<dphiyx_100111<<" +- "<<edphiyx_100111<<"  "<<dphizx_100111<<" +- "<<edphizx_100111<<endl<<endl;

cout<<endl<<"Starting 1000_100001: "<<endl;
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY);
fitter.fit();
double dx_100001, edx_100001, dphizx_100001, edphizx_100001;
dx_100001 = fitter.value(MuonResiduals5DOFFitter::kAlignX)*10;
edx_100001 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignX)*10;
dphizx_100001 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
edphizx_100001 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
cout<<"1000_100001: "<<dx_100001<<" +- "<<edx_100001<<"  "<<dphizx_100001<<" +- "<<edphizx_100001<<endl<<endl;

cout<<endl<<"Starting 1000_100000: "<<endl;
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiZ);
fitter.fit();
double dx_100000, edx_100000;
dx_100000 = fitter.value(MuonResiduals5DOFFitter::kAlignX)*10;
edx_100000 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignX)*10;
cout<<"1000_100000: "<<dx_100000<<" +- "<<edx_100000<<endl<<endl;



cout<<endl<<"Starting 0010_000011: "<<endl;
fitter.useRes(MuonResidualsFitter::k0010);
fitter.fix(MuonResiduals5DOFFitter::kAlignX);
fitter.fix(MuonResiduals5DOFFitter::kAlignZ);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiZ, 0);
fitter.fix(MuonResiduals5DOFFitter::kResidSigma);
fitter.fix(MuonResiduals5DOFFitter::kResSlopeSigma,0);
fitter.fit();
double dphiydxdz, dphizdxdz, edphiydxdz, edphizdxdz;
dphiydxdz = fitter.value(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
edphiydxdz = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
dphizdxdz = fitter.value(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
edphizdxdz = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
cout<<"0010_000011: "<<dphiydxdz<<" +- "<<edphiydxdz<<"  "<<dphizdxdz<<" +- "<<edphizdxdz<<endl<<endl;

cout<<endl<<"Starting 0010_000111: "<<endl;
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiZ, 0);
fitter.fit();
double dphixdxdz_000111, edphixdxdz_000111, dphiydxdz_000111, edphiydxdz_000111, dphizdxdz_000111, edphizdxdz_000111;
dphixdxdz_000111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiX)*1000;
edphixdxdz_000111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiX)*1000;
dphiydxdz_000111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
edphiydxdz_000111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
dphizdxdz_000111 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
edphizdxdz_000111 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiZ)*1000;
cout<<"0010_000111: "<<dphixdxdz_000111<<" +- "<<edphixdxdz_000111<<"  "<<dphiydxdz_000111<<" +- "<<edphiydxdz_000111<<"  "<<dphizdxdz_000111<<" +- "<<edphizdxdz_000111<<endl<<endl;

cout<<endl<<"Starting 0010_000010: "<<endl;
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiZ);
fitter.fit();
double dphiydxdz_000010, edphiydxdz_000010;
dphiydxdz_000010 = fitter.value(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
edphiydxdz_000010 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignPhiY)*1000;
cout<<"0010_000010: "<<dphiydxdz_000010<<" +- "<<edphiydxdz_000010<<endl<<endl;



cout<<endl<<"Starting 1000_101000: "<<endl;
fitter.useRes(MuonResidualsFitter::k1000);
fitter.fix(MuonResiduals5DOFFitter::kAlignX, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignZ, 0);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals5DOFFitter::kAlignPhiZ);
fitter.fix(MuonResiduals5DOFFitter::kResidSigma, 0);
fitter.fix(MuonResiduals5DOFFitter::kResSlopeSigma);
fitter.fit();
double dx_101000, edx_101000, dz_101000, edz_101000;
dx_101000 = fitter.value(MuonResiduals5DOFFitter::kAlignX)*10;
edx_101000 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignX)*10;
dz_101000 = fitter.value(MuonResiduals5DOFFitter::kAlignZ)*10;
edz_101000 = fitter.errorerror(MuonResiduals5DOFFitter::kAlignZ)*10;
cout<<"1000_101000: "<<dx_101000<<" +- "<<edx_101000<<"  "<<dz_101000<<" +- "<<edz_101000<<endl<<endl;




//tt->Draw("angle_y:pos_y","","");
tt->Draw("track_dydz:track_y","","");
TGraph *gr = (TGraph*)TVirtualPad::Pad()->GetPrimitive("Graph");
TF1 fdy("fdy","pol1",-110,110);
gr.Fit("fdy","R");
double D = 23.5;
double c = fdy.GetParameter(0);
double k = fdy.GetParameter(1);
double db = k*23.5*(dphizx - dphizdxdz);
double edb = fabs(k)*23.5*sqrt(edphizx*edphizx + edphizdxdz*edphizdxdz);
double dai = D/100.*(dphiydxdz - dphiyx - c*(dphizdxdz - dphizx));
double edai = D/100.*sqrt(edphiydxdz*edphiydxdz + edphiyx*edphiyx + c*c*(edphizdxdz*edphizdxdz + edphizx*edphizx));


char cname[30];
sprintf(cname,"MB%+d_%d_%02d",wh,st,sec);

fstream fstr;
fstr.open (res_fname.Data(), fstream::out | fstream::app);
fstr<<cname<<" "<<wh<<" "<<st<<" "<<sec<<"    "<<db<<" "<<edb<<"  "<<dai<<" "<<edai<<"   "<<0<<" "<<0<<"  "<<k
  <<"    "<<dx_100000<<" "<<edx_100000
  <<"    "<<dx_100001<<" "<<edx_100001<<"  "<<dphizx_100001<<" "<<edphizx_100001
  <<"    "<<dx<<" "<<edx<<"  "<<dphiyx<<" "<<edphiyx<<"  "<<dphizx<<" "<<edphizx
  <<"    "<<dx_100111<<" "<<edx_100111<<"  "<<dphixx_100111<<" "<<edphixx_100111<<"  "<<dphiyx_100111<<" "<<edphiyx_100111<<"  "<<dphizx_100111<<" "<<edphizx_100111
  <<"    "<<dx_101000<<" "<<edx_101000<<"  "<<dz_101000<<" "<<edz_101000
  <<"    "<<0<<" "<<0
  <<"    "<<0<<" "<<0<<"  "<<0<<" "<<0
  <<"    "<<0<<" "<<0<<"  "<<0<<" "<<0<<"  "<<0<<" "<<0
  <<"    "<<0<<" "<<0<<"  "<<0<<" "<<0<<"  "<<0<<" "<<0<<"  "<<0<<" "<<0
  <<"    "<<0<<" "<<0<<"  "<<0<<" "<<0
  <<"    "<<dx_101000<<" "<<edx_101000<<"  "<<0<<" "<<0<<"  "<<dz_101000<<" "<<edz_101000
  <<"    "<<dphiydxdz_000010<<" "<<edphiydxdz_000010
  <<"    "<<dphiydxdz<<" "<<edphiydxdz<<"  "<<dphizdxdz<<" "<<edphizdxdz
  <<"    "<<dphixdxdz_000111<<" "<<edphixdxdz_000111<<"  "<<dphiydxdz_000111<<" "<<edphiydxdz_000111<<"  "<<dphizdxdz_000111<<" "<<edphizdxdz_000111
  <<endl;
fstr.close();


cout<< setiosflags(ios::fixed) <<setprecision(4);

cout<<endl;
cout<<"1000_100000: "<<dx_100000<<" +- "<<edx_100000<<endl;
cout<<"1000_100001: "<<dx_100001<<" +- "<<edx_100001<<"  "<<dphizx_100001<<" +- "<<edphizx_100001<<endl;
cout<<"1000_100011: "<<dx<<" +- "<<edx<<"  "<<dphiyx<<" +- "<<edphiyx<<"  "<<dphizx<<" +- "<<edphizx<<endl;
cout<<"1000_100111: "<<dx_100111<<" +- "<<edx_100111<<"  "<<dphixx_100111<<" +- "<<edphixx_100111<<"  "<<dphiyx_100111<<" +- "<<edphiyx_100111<<"  "<<dphizx_100111<<" +- "<<edphizx_100111<<endl;
cout<<"1000_101000: "<<dx_101000<<" +- "<<edx_101000<<"  "<<dz_101000<<" +- "<<edz_101000<<endl<<endl;

cout<<"0010_000010: "<<dphiydxdz_000010<<" +- "<<edphiydxdz_000010<<endl;
cout<<"0010_000011: "<<dphiydxdz<<" +- "<<edphiydxdz<<"  "<<dphizdxdz<<" +- "<<edphizdxdz<<endl;
cout<<"0010_000111: "<<dphixdxdz_000111<<" +- "<<edphixdxdz_000111<<"  "<<dphiydxdz_000111<<" +- "<<edphiydxdz_000111<<"  "<<dphizdxdz_000111<<" +- "<<edphizdxdz_000111<<endl<<endl;

}
