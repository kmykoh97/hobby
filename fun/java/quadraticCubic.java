class quadraticCubic {

  static int quadratic(int a, int b, int c) {
    System.out.println("Solving quadratic equation");
    int x = b*b - 4*a*c;
    int solution1 = (-b + (b*b - 4*a*c)) / 2*a;
    int solution2 = (-b - (b*b - 4*a*c)) / 2*a;
    if(x < 0) {
      return 0;
    } else if(x == 0) {
      return solution1;
    } else {
      return solution2;
    }
  }

  static int cubic(int a, int b, int c, int d) {
    System.out.println("Solving cubic equation");
    int x = b*b - 4*a*c;
    int solution1 = (-b + (b*b - 4*a*c)) / 2*a;
    int solution2 = (-b - (b*b - 4*a*c)) / 2*a;
  }

  public static void main(String[] args) {
    
    int result = quadratic(1, 2, 1);
    System.out.println(result);
  }

}
