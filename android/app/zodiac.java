import java.util.Scanner;
import java.util.*;

/*Please enter your birth year (1936 to 2018 only) and I will tell you your zodiac Chinese animal and your personality traits!
By the way this is my first program so suggestions are welcomed!Have fun and enjoy!*/

public class ChineseZodiacAnimals {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int birth_year=0;
        System.out.println("Plese enter your birth_year:");
        Scanner scanner=new Scanner(System.in);

        try{
        birth_year=scanner.nextInt();
        if(birth_year==1936||birth_year==1948||birth_year==1960||birth_year==1972||birth_year==1984||birth_year==1996||birth_year==2008)
            System.out.println("You are born in the year of shu(rat)in Chinese year and you are quick-witted,resourceful and versatile!");
        else if(birth_year==1937||birth_year==1949||birth_year==1961||birth_year==1973||birth_year==1985||birth_year==1997||birth_year==2009)
            System.out.println("You are born in the year of niu(ox)in Chinese year and you are decisive,honest,dependable and hardworking!");
        else if(birth_year==1938||birth_year==1950||birth_year==1962||birth_year==1974||birth_year==1986||birth_year==1998||birth_year==2010)
            System.out.println("You are born in the year of hu(tiger)in Chinese year and you are brave,competitive,unpredictable and self-confident!");
        else if(birth_year==1939||birth_year==1951||birth_year==1963||birth_year==1975||birth_year==1987||birth_year==1999||birth_year==2011)
            System.out.println("You are born in the year of tu(rabbit)in Chinese year and you are gentle,quiet,elegant,alert,quick,skillful,kind and patient!");
        else if(birth_year==1940||birth_year==1952||birth_year==1964||birth_year==1976||birth_year==1988||birth_year==2000||birth_year==2012)
            System.out.println("You are born in the year of long(dragon)in Chinese year and you are confident,intelligent,ambitious,presevering and hardworking!");
        else if(birth_year==1941||birth_year==1953||birth_year==1965||birth_year==1977||birth_year==1989||birth_year==2001||birth_year==2013)
            System.out.println("You are born in the year of she(snake)in Chinese year and you are intelligent,courageous,confident,insightful and communicative!");
        else if(birth_year==1942||birth_year==1954||birth_year==1966||birth_year==1978||birth_year==1990||birth_year==2002||birth_year==2014)
            System.out.println("You are born in the year of ma(horse)in Chinese year and you are animated,kind,straightforward,active and energetic!");
        else if(birth_year==1943||birth_year==1955||birth_year==1967||birth_year==1979||birth_year==1991||birth_year==2003||birth_year==2015)
            System.out.println("You are born in the year of yang(goat)in Chinese year and you are gentle,shy,stable,sympathetic and adventurous!");
        else if(birth_year==1944||birth_year==1956||birth_year==1968||birth_year==1980||birth_year==1992||birth_year==2004||birth_year==2016)
            System.out.println("You are born in the year of hou(monkey)in Chinese year and you are witty,intelligent,ambitious and adventurous!");
        else if(birth_year==1945||birth_year==1957||birth_year==1969||birth_year==1981||birth_year==1993||birth_year==2005||birth_year==2017)
            System.out.println("You are born in the year of ji(rooster)in Chinese year and you are observant,hardworking,resourceful,courageous and talented!");
        else if(birth_year==1946||birth_year==1958||birth_year==1970||birth_year==1982||birth_year==1994||birth_year==2006||birth_year==2018)
            System.out.println("You are born in the year of gou(dog)in Chinese year and you are loyal,honest,amiable,kind,cautious and prudent!");
        else
            System.out.println("You are born in the year of zhu(pig)in Chinese year and you are diligen,compassionate,generous,easy-going and gentle!");

        }
        catch(InputMismatchException e){
            System.out.println("Error in the input...please enter your birth_year");
        }

    }





}
