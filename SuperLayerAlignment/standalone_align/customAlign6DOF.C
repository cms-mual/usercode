{
#include <iomanip>

gROOT->SetBatch(1);

//int wh = 0, st = 3, sec = 7;
//TString res_fname="res.txt";
//TString fname = "../data_1110_110011_dumpfid_corphiz13_01.root";
//TString fname = "data_1110_110011_dumpfidtt_01.root";

gSystem->Load("libFit.so");

cout<<endl<<"Starting 1000_100011: "<<endl;
MuonResiduals6DOFFitter fitter(MuonResidualsFitter::kPureGaussian, 1, MuonResidualsFitter::k1000, false);
tt = fitter.readNtuple(fname.Data(), wh, st, sec);
fitter.fix(MuonResiduals6DOFFitter::kAlignY);
fitter.fix(MuonResiduals6DOFFitter::kAlignZ);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fit();
double dx, dphiyx, dphizx, edx, edphiyx, edphizx;
dx = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
dphiyx = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiyx = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizx = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizx = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<endl<<"1000_100011: "<<dx<<" +- "<<edx<<"  "<<dphiyx<<" +- "<<edphiyx<<"  "<<dphizx<<" +- "<<edphizx<<endl<<endl;

double saved_AlignPhiY = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY);

cout<<endl<<"Starting 1000_100111: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX,0);
fitter.fit();
double dx_100111, edx_100111, dphixx_100111, edphixx_100111, dphiyx_100111, edphiyx_100111, dphizx_100111, edphizx_100111;
dx_100111 = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx_100111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
dphixx_100111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
edphixx_100111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
dphiyx_100111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiyx_100111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizx_100111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizx_100111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"1000_100111: "<<dx_100111<<" +- "<<edx_100111<<"  "<<dphixx_100111<<" +- "<<edphixx_100111<<"  "<<dphiyx_100111<<" +- "<<edphiyx_100111<<"  "<<dphizx_100111<<" +- "<<edphizx_100111<<endl<<endl;

cout<<endl<<"Starting 1000_100001: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fit();
double dx_100001, edx_100001, dphizx_100001, edphizx_100001;
dx_100001 = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx_100001 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
dphizx_100001 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizx_100001 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"1000_100001: "<<dx_100001<<" +- "<<edx_100001<<"  "<<dphizx_100001<<" +- "<<edphizx_100001<<endl<<endl;

cout<<endl<<"Starting 1000_100000: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ);
fitter.fit();
double dx_100000, edx_100000;
dx_100000 = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx_100000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
cout<<"1000_100000: "<<dx_100000<<" +- "<<edx_100000<<endl<<endl;


cout<<endl<<"Starting 0100_010001: "<<endl;
fitter.useRes(MuonResidualsFitter::k0100);
//fitter.setInitialValue(MuonResiduals6DOFFitter::kAlignPhiY, saved_AlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignY,0);
fitter.fix(MuonResiduals6DOFFitter::kAlignX);
fitter.fix(MuonResiduals6DOFFitter::kResidYSigma,0);
fitter.fix(MuonResiduals6DOFFitter::kResidXSigma);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ, 0);
fitter.fit();
double dy, dphiyy, dphizy, edy, edphiyy, edphizy;
dy = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dphizy = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizy = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"0100_010001: "<<dy<<" +- "<<edy<<"  "<<dphizy<<" +- "<<edphizy<<endl<<endl;

cout<<endl<<"Starting 0100_010011: "<<endl;
fitter.setInitialValue(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY,0);
fitter.fit();
double dy_010011, edy_010011, dphixy_010011, edphixy_010011, dphiyy_010011, edphiyy_010011, dphizy_010011, edphizy_010011;
dy_010011 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_010011 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dphiyy_010011 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiyy_010011 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizy_010011 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizy_010011 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"0100_010011: "<<dy_010011<<" +- "<<edy_010011<<"  "<<dphiyy_010011<<" +- "<<edphiyy_010011<<"  "<<dphizy_010011<<" +- "<<edphizy_010011<<endl<<endl;


cout<<endl<<"Starting 0100_010100: "<<endl;
fitter.setInitialValue(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX,0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ);
fitter.fit();
double dy_010100, edy_010100, dphixy_010100, edphixy_010100;
dy_010100 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_010100 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dphixy_010100 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
edphixy_010100 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
cout<<"0100_010100: "<<dy_010100<<" +- "<<edy_010100<<"  "<<dphixy_010100<<" +- "<<edphixy_010100<<endl<<endl;


cout<<endl<<"Starting 0100_010111: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ, 0);
fitter.fit();
double dy_010111, edy_010111, dphixy_010111, edphixy_010111, dphiyy_010111, edphiyy_010111, dphizy_010111, edphizy_010111;
dy_010111 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_010111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dphixy_010111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
edphixy_010111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
dphiyy_010111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiyy_010111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizy_010111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizy_010111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"0100_010111: "<<dy_010111<<" +- "<<edy_010111<<"  "<<dphixy_010111<<" +- "<<edphixy_010111<<"  "<<dphiyy_010111<<" +- "<<edphiyy_010111<<"  "<<dphizy_010111<<" +- "<<edphizy_010111<<endl<<endl;

cout<<endl<<"Starting 0100_010000: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ);
fitter.fit();
double dy_010000, edy_010000;
dy_010000 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_010000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
cout<<"0100_010000: "<<dy_010000<<" +- "<<edy_010000<<endl<<endl;


cout<<endl<<"Starting 0010_000011: "<<endl;
fitter.useRes(MuonResidualsFitter::k0010);
fitter.setInitialValue(MuonResiduals6DOFFitter::kAlignPhiY, 0.);
fitter.fix(MuonResiduals6DOFFitter::kAlignY);
fitter.fix(MuonResiduals6DOFFitter::kResidYSigma);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ, 0);
fitter.fix(MuonResiduals6DOFFitter::kResSlopeXSigma, 0);
fitter.fit();
double dphiydxdz, dphizdxdz, edphiydxdz, edphizdxdz;
dphiydxdz = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiydxdz = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizdxdz = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizdxdz = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"0010_000011: "<<dphiydxdz<<" +- "<<edphiydxdz<<"  "<<dphizdxdz<<" +- "<<edphizdxdz<<endl<<endl;

cout<<endl<<"Starting 0010_000111: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ, 0);
fitter.fit();
double dphixdxdz_000111, edphixdxdz_000111, dphiydxdz_000111, edphiydxdz_000111, dphizdxdz_000111, edphizdxdz_000111;
dphixdxdz_000111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
edphixdxdz_000111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiX)*1000;
dphiydxdz_000111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiydxdz_000111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
dphizdxdz_000111 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
edphizdxdz_000111 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiZ)*1000;
cout<<"0010_000111: "<<dphixdxdz_000111<<" +- "<<edphixdxdz_000111<<"  "<<dphiydxdz_000111<<" +- "<<edphiydxdz_000111<<"  "<<dphizdxdz_000111<<" +- "<<edphizdxdz_000111<<endl<<endl;

cout<<endl<<"Starting 0010_000010: "<<endl;
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ);
fitter.fit();
double dphiydxdz_000010, edphiydxdz_000010;
dphiydxdz_000010 = fitter.value(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
edphiydxdz_000010 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignPhiY)*1000;
cout<<"0010_000010: "<<dphiydxdz_000010<<" +- "<<edphiydxdz_000010<<endl<<endl;


cout<<endl<<"Starting 1000_101000: "<<endl;
fitter.useRes(MuonResidualsFitter::k1000);
fitter.fix(MuonResiduals6DOFFitter::kAlignX, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignY);
fitter.fix(MuonResiduals6DOFFitter::kAlignZ, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiX);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiY);
fitter.fix(MuonResiduals6DOFFitter::kAlignPhiZ);
fitter.fix(MuonResiduals6DOFFitter::kResidXSigma, 0);
fitter.fix(MuonResiduals6DOFFitter::kResSlopeXSigma);
fitter.fit();
double dx_101000, edx_101000, dz_101000, edz_101000;
dx_101000 = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx_101000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
dz_101000 = fitter.value(MuonResiduals6DOFFitter::kAlignZ)*10;
edz_101000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignZ)*10;
cout<<"1000_101000: "<<dx_101000<<" +- "<<edx_101000<<"  "<<dz_101000<<" +- "<<edz_101000<<endl<<endl;


cout<<endl<<"Starting 0100_011000: "<<endl;
fitter.useRes(MuonResidualsFitter::k0100);
fitter.fix(MuonResiduals6DOFFitter::kAlignX);
fitter.fix(MuonResiduals6DOFFitter::kAlignY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignZ, 0);
fitter.fix(MuonResiduals6DOFFitter::kResidXSigma);
fitter.fix(MuonResiduals6DOFFitter::kResidYSigma, 0);
fitter.fix(MuonResiduals6DOFFitter::kResSlopeXSigma);
fitter.fit();
double dy_011000, edy_011000, dz_011000, edz_011000;
dy_011000 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_011000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dz_011000 = fitter.value(MuonResiduals6DOFFitter::kAlignZ)*10;
edz_011000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignZ)*10;
cout<<"0100_011000: "<<dy_011000<<" +- "<<edy_011000<<"  "<<dz_011000<<" +- "<<edz_011000<<endl<<endl;


cout<<endl<<"Starting 1100_111000: "<<endl;
fitter.useRes(MuonResidualsFitter::k1100);
fitter.fix(MuonResiduals6DOFFitter::kAlignX, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignY, 0);
fitter.fix(MuonResiduals6DOFFitter::kAlignZ, 0);
fitter.fix(MuonResiduals6DOFFitter::kResidXSigma, 0);
fitter.fix(MuonResiduals6DOFFitter::kResidYSigma, 0);
fitter.fit();
double dx_111000, edx_111000, dy_111000, edy_111000, dz_111000, edz_111000;
dx_111000 = fitter.value(MuonResiduals6DOFFitter::kAlignX)*10;
edx_111000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignX)*10;
dy_111000 = fitter.value(MuonResiduals6DOFFitter::kAlignY)*10;
edy_111000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignY)*10;
dz_111000 = fitter.value(MuonResiduals6DOFFitter::kAlignZ)*10;
edz_111000 = fitter.errorerror(MuonResiduals6DOFFitter::kAlignZ)*10;
cout<<"1100_111000: "<<dx_111000<<" +- "<<edx_111000<<"  "<<dy_111000<<" +- "<<edy_111000<<"  "<<dz_111000<<" +- "<<edz_111000<<endl<<endl;



//tt->Draw("angle_y:pos_y","","");
tt->Draw("track_dydz:track_y","","");
TGraph *gr = (TGraph*)TVirtualPad::Pad()->GetPrimitive("Graph");
TF1 fdy("fdy","pol1",-110,110);
gr.Fit("fdy","R");
double D = 23.5;
double c = fdy.GetParameter(0);
double k = fdy.GetParameter(1);
double db = k*D*(dphizx - dphizdxdz);
double edb = fabs(k)*D*sqrt(edphizx*edphizx + edphizdxdz*edphizdxdz);
double dai = D/100.*(dphiydxdz - dphiyx - c*(dphizdxdz - dphizx));
double edai = D/100.*sqrt(edphiydxdz*edphiydxdz + edphiyx*edphiyx + c*c*(edphizdxdz*edphizdxdz + edphizx*edphizx));

char cname[30];
sprintf(cname,"MB%+d_%d_%02d",wh,st,sec);

fstream fstr;
fstr.open (res_fname.Data(), fstream::out | fstream::app);
fstr<<cname<<" "<<wh<<" "<<st<<" "<<sec<<"    "<<db<<" "<<edb<<"  "<<dai<<" "<<edai<<"   "<<dphizy-dphizx<<" "<<sqrt(edphizy*edphizy+edphizx*edphizx)<<"  "<<k
  <<"    "<<dx_100000<<" "<<edx_100000
  <<"    "<<dx_100001<<" "<<edx_100001<<"  "<<dphizx_100001<<" "<<edphizx_100001
  <<"    "<<dx<<" "<<edx<<"  "<<dphiyx<<" "<<edphiyx<<"  "<<dphizx<<" "<<edphizx
  <<"    "<<dx_100111<<" "<<edx_100111<<"  "<<dphixx_100111<<" "<<edphixx_100111<<"  "<<dphiyx_100111<<" "<<edphiyx_100111<<"  "<<dphizx_100111<<" "<<edphizx_100111
  <<"    "<<dx_101000<<" "<<edx_101000<<"  "<<dz_101000<<" "<<edz_101000
  <<"    "<<dy_010000<<" "<<edy_010000
  <<"    "<<dy<<" "<<edy<<"  "<<dphizy<<" "<<edphizy
  <<"    "<<dy_010011<<" "<<edy_010011<<"  "<<dphiyy_010011<<" "<<edphiyy_010011<<"  "<<dphizy_010011<<" "<<edphizy_010011
  <<"    "<<dy_010111<<" "<<edy_010111<<"  "<<dphixy_010111<<" "<<edphixy_010111<<"  "<<dphiyy_010111<<" "<<edphiyy_010111<<"  "<<dphizy_010111<<" "<<edphizy_010111
  <<"    "<<dy_011000<<" "<<edy_011000<<"  "<<dz_011000<<" "<<edz_011000
  <<"    "<<dx_111000<<" "<<edx_111000<<"  "<<dy_111000<<" "<<edy_111000<<"  "<<dz_111000<<" "<<edz_111000
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


cout<<"0100_010000: "<<dy_010000<<" +- "<<edy_010000<<endl;
cout<<"0100_010001: "<<dy<<" +- "<<edy<<"  "<<dphizy<<" +- "<<edphizy<<endl;
cout<<"0100_010011: "<<dy_010011<<" +- "<<edy_010011<<"  "<<dphiyy_010011<<" +- "<<edphiyy_010011<<"  "<<dphizy_010011<<" +- "<<edphizy_010011<<endl;
cout<<"0100_010111: "<<dy_010111<<" +- "<<edy_010111<<"  "<<dphixy_010111<<" +- "<<edphixy_010111<<"  "<<dphiyy_010111<<" +- "<<edphiyy_010111<<"  "<<dphizy_010111<<" +- "<<edphizy_010111<<endl;
cout<<"0100_011000: "<<dy_011000<<" +- "<<edy_011000<<"  "<<dz_011000<<" +- "<<edz_011000<<endl;
cout<<"0100_010100: "<<dy_010100<<" +- "<<edy_010100<<"  "<<dphixy_010100<<" +- "<<edphixy_010100<<endl<<endl;

cout<<"1100_111000: "<<dx_111000<<" +- "<<edx_111000<<"  "<<dy_111000<<" +- "<<edy_111000<<"  "<<dz_111000<<" +- "<<edz_111000<<endl<<endl;

cout<<"0010_000010: "<<dphiydxdz_000010<<" +- "<<edphiydxdz_000010<<endl;
cout<<"0010_000011: "<<dphiydxdz<<" +- "<<edphiydxdz<<"  "<<dphizdxdz<<" +- "<<edphizdxdz<<endl;
cout<<"0010_000111: "<<dphixdxdz_000111<<" +- "<<edphixdxdz_000111<<"  "<<dphiydxdz_000111<<" +- "<<edphiydxdz_000111<<"  "<<dphizdxdz_000111<<" +- "<<edphizdxdz_000111<<endl<<endl;

}
