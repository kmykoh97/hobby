// Zodiac Program
// Created by MyKoh
// 2017-12-7

import java.util.Scanner;
import java.util.*;

/*Enter your birth year
I will tell you your Chinise Zodiac and your personality traits!*/

class zodiac {

  public static main(String[] args) {
    int birthYear = 0;
    System.out.println("Plese enter your year of birth:");
    Scanner userInput = new Scanner(System.in);
    try {
      birthYear = userInput.nextInt();
      int remainder = birthYear % 12;
      switch(remainder) {
        case 0:
          return("You are born in the year of hou(monkey)in Chinese year and you are witty,intelligent,ambitious and adventurous!");
        case 1:
          return("You are born in the year of ji(rooster)in Chinese year and you are observant,hardworking,resourceful,courageous and talented!");
        case 2:
          return("You are born in the year of gou(dog)in Chinese year and you are loyal,honest,amiable,kind,cautious and prudent!");
        case 3:
          return("You are born in the year of zhu(pig)in Chinese year and you are diligen,compassionate,generous,easy-going and gentle!");
        case 4:
          return("You are born in the year of shu(rat)in Chinese year and you are quick-witted,resourceful and versatile!");
        case 5:
          return("You are born in the year of niu(ox)in Chinese year and you are decisive,honest,dependable and hardworking!");
        case 6:
          return("You are born in the year of hu(tiger)in Chinese year and you are brave,competitive,unpredictable and self-confident!");
        case 7:
          return("You are born in the year of tu(rabbit)in Chinese year and you are gentle,quiet,elegant,alert,quick,skillful,kind and patient!");
        case 8:
          return("You are born in the year of long(dragon)in Chinese year and you are confident,intelligent,ambitious,presevering and hardworking!");
        case 9:
          return("You are born in the year of she(snake)in Chinese year and you are intelligent,courageous,confident,insightful and communicative!");
        case 10:
          return("You are born in the year of ma(horse)in Chinese year and you are animated,kind,straightforward,active and energetic!");
        case 11:
          return("You are born in the year of yang(goat)in Chinese year and you are gentle,shy,stable,sympathetic and adventurous!");
      }
    } catch(InputMismatchException e){
        System.out.println("Error in the input...please enter your year of birth:");
      }
  }
}
