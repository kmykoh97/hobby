// Zodiac Program
// Created by MyKoh
// 2017-12-7

import java.util.Scanner;
import java.util.*;

/*Enter your birth year
I will tell you your Chinise Zodiac and your personality traits!*/

class zodiac {

  public static void main(String[] args) {
    int birthYear = 0;
    System.out.println("Plese enter your year of birth:");
    Scanner userInput = new Scanner(System.in);
    try {
      birthYear = userInput.nextInt();
      int remainder = birthYear % 12;
      switch(remainder) {
        case 0:
          System.out.println("You are born in the year of hou(monkey)in Chinese year and you are witty,intelligent,ambitious and adventurous!");
          break;
        case 1:
          System.out.println("You are born in the year of ji(rooster)in Chinese year and you are observant,hardworking,resourceful,courageous and talented!");
          break;
        case 2:
          System.out.println("You are born in the year of gou(dog)in Chinese year and you are loyal,honest,amiable,kind,cautious and prudent!");
          break;
        case 3:
          System.out.println("You are born in the year of zhu(pig)in Chinese year and you are diligen,compassionate,generous,easy-going and gentle!");
          break;
        case 4:
          System.out.println("You are born in the year of shu(rat)in Chinese year and you are quick-witted,resourceful and versatile!");
          break;
        case 5:
          System.out.println("You are born in the year of niu(ox)in Chinese year and you are decisive,honest,dependable and hardworking!");
          break;
        case 6:
          System.out.println("You are born in the year of hu(tiger)in Chinese year and you are brave,competitive,unpredictable and self-confident!");
          break;
        case 7:
          System.out.println("You are born in the year of tu(rabbit)in Chinese year and you are gentle,quiet,elegant,alert,quick,skillful,kind and patient!");
          break;
        case 8:
          System.out.println("You are born in the year of long(dragon)in Chinese year and you are confident,intelligent,ambitious,presevering and hardworking!");
          break;
        case 9:
          System.out.println("You are born in the year of she(snake)in Chinese year and you are intelligent,courageous,confident,insightful and communicative!");
          break;
        case 10:
          System.out.println("You are born in the year of ma(horse)in Chinese year and you are animated,kind,straightforward,active and energetic!");
          break;
        case 11:
          System.out.println("You are born in the year of yang(goat)in Chinese year and you are gentle,shy,stable,sympathetic and adventurous!");
          break;
      }
    } catch(InputMismatchException e){
        System.out.println("Error in the input...please enter your year of birth:");
      }
  }
}
