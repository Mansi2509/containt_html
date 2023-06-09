# class OverloadingExample:{
#     static int add(int a,int b)
#     {
#         return a+b;
#     }static int add(int a,int b,int c)
#     {
#         return a+b+c;
#     }  
# }  

class Overloading {
    static int add(int a, int b) {
        return a + b;
    }

    static int add(int a, int b, int c) {
        return a + b + c;
    }
}

class Animal {
    void eat() {
        System.out.println("eating...");
    }
}

class Dog extends Animal {
    void eat() {
        System.out.println("eating bread...");
    }
}