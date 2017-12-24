
class quadraticCubic {

  static double quadratic(double a, double b, double c) {
    System.out.println("Solving quadratic equation");
    double x = b*b - 4*a*c;
    double solution1 = (-b + Math.pow(x, 0.5)) / 2*a;
    double solution2 = (-b - Math.pow(x, 0.5)) / 2*a;
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
    double p = -b/(3*a);
    double q = p*p*p + (b*c-3*a*d)/(6*a*a);
    double r = c/(3*a);
    double x = (Math.pow((q+Math.pow((q*q+(r-p*p)*(r-p*p)*(r-p*p))), 0.5), (1/3)) + Math.pow((q-Math.pow((q*q+(r-p*p)*(r-p*p)*(r-p*p))), 0.5), (1/3)) + p);
    return x;
  }

  static int determineSquareCubic(int a, int b, int c, int d) {
    // return value explanation:
    // case 0: linear equation
    // case 1: quadratic equation
    // case 2: cubic equation
    // System.out.println("function to determine if user's input is quadratic or cubic");
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
    switch(determineSquareCubic(a, b, c, d)) {
      case 0:
        System.out.println("Linear Equation!");
      case 1:
        double result1 = quadratic(a, b, c);
        System.out.println(result1);
      case 2:
        double result2 = cubic(a, b, c, d);
        System.out.println(result2);
    }
  }
}
