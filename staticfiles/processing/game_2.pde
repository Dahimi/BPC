void setup(){
    BOT myBOT = new BOT(40, 40);

}

void StartSimulation(String data){

  BOT myBOT = new BOT(40, 40);
  String[] data_list = data.split(" ");

  for(int index=0; index < data.length; index+=1){
       String[] coor = data_list[index].split(",");
        int newX=int(coor[0]);
        int newY=int(coor[1]);
        myBOT.draw_function(newX, newY);
  }
}

void waitasec (int sec) {

   int minutes = minute();
   int seconds = second();
   int hour = hour();
   int starttime = (hour * 3600) + (minutes * 60) + seconds;
   int finaltime = starttime + sec;

   while (starttime < finaltime) {

       minutes = minute();
       seconds = second();
       starttime = (hour * 3600) + (minutes * 60) + seconds;
   }
}


class BOT {
  int x, y;
  BOT(int initX, int initY) {
    x = initX;
    y = initY;
    draw_function(x, y);
  }

  void setup(){
  background(255);
    int step = 0;
    size(500,500);
    for(step=0;step<500;step+=20){
      line(step, 0, step, 500);
      line(0, step, 500, step);
    }
  }
  void draw_function(int new_x, int new_y) {
    setup();
    fill(255, 255, 0);
    ellipse(new_x, new_y, 20, 20);
  }

}