package classes;

public class PlayingWithShapes {

	
	public static void main (String[] args) {
		Rectangle r = new Rectangle(3,5,"Blue");
		Circle c1 = new Circle(3.5, "Red");
		Circle c2 = new Circle(12.5);
			
		System.out.println("The height of r is: "+r.getHeight());
		System.out.println("The color of r is: "+r.getColor());
		System.out.println("The radius of c1 is: "+c1.getRadius());
		System.out.println("The color of c2 is: "+c2.getColor());
	}
}
