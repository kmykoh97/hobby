class quadraticCubic {

  static double quadratic(double a, double b, double c) {
    System.out.println("Solving quadratic equation");
    double x = b*b - 4*a*c;
    double solution1 = (-b + (b*b - 4*a*c)) / 2*a;
    double solution2 = (-b - (b*b - 4*a*c)) / 2*a;
    if(x < 0) {
      return 0;
    } else if(x == 0) {
      return solution1;
    } else {
      return solution2;
    }
  }

  static double cubic(double a, double b, double c, double d) {
    System.out.println("Solving cubic equation");
    double x = b*b - 4*a*c;
    double solution1 = (-b + (b*b - 4*a*c)) / 2*a;
    double solution2 = (-b - (b*b - 4*a*c)) / 2*a;
    double solution3 = (-b - (b*b - 4*a*c)) / 2*a;
    return '1';
  }

  static int determineSquareCubic(int a, int b, int c, int d) {
    // return value explanation:
    // case 0: linear equation
    // case 1: quadratic equation
    // case 2: cubic equation
    System.out.println("function to determine if user's input is quadratic or cubic");
    if(a == 0) {
      return 0;
    } else if(d == 0) {
      return 1;
    } else {
      return 2;
    }
  }

  public static void main(String[] args) {
    // to determine equation type:
    int a = 1;
    int b = 2;
    int c = 1;
    int d = 0;
    switch(determineSquareCubic) {
      case 0:
      System.out.println('Linear Equation!');
      case 1:
      int result = quadratic(a, b, c);
      System.out.println(result);
      case 2:
      int result = cubic(a, b, c, d);
      System.out.println(result);
    }
  }

}
