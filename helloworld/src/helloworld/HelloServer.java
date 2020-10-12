package helloworld;
import java.rmi.* ;
public class HelloServer 
{
 public static void main(String[] args) 
		 {
		  try 
			  { /* créer une instance de la classe Hello et
					  l'enregistrer dans le serveur de noms */
					Naming.rebind("Hello1", new HelloImpl("Hello world"));
					System.out.println("Serveur prêt") ;
					                                                                
			  }
			  catch (Exception e) { System.out.println("Erreur serveur : " + e) ; }
		}
}