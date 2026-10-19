// Independent lift-off hood. Units mm; print mode is roof-down.
clear_height=110; // provisional: 88 hardware envelope + 22 relaxed-wire allowance
wall=2;
mode="print"; // print, assembly, cutaway
assert(clear_height>=88);
module hood(){
 difference(){
  union(){
   difference(){
    translate([-47,-47,0]) cube([94,94,clear_height+wall]);
    translate([-45,-45,-0.1]) cube([90,90,clear_height+0.1]);
   }
   // Full-height baffle overlaps right wall and roof; no hanging wall in print pose.
   translate([10,31,0]) cube([36,2,clear_height+1]);
  }
  translate([25,44.99,-0.1]) cube([16,3.1,10.1]);
 }
}
module assembly_hood(){translate([6,-7,0]) hood();}
if(mode=="print") translate([0,0,clear_height+wall]) rotate([180,0,0]) hood();
else {
 color([0.15,0.17,0.2])
 if(mode=="cutaway") difference(){assembly_hood();translate([-60,-65,0]) cube([120,60,130]);}
 else assembly_hood();
}
