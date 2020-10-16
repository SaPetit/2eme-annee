Interface ServeurTchatInterface extends Remote
{
    public void enregistrerClient(String pseudo, ClientInterface refClient);
    public void enregistrerClientAlt(String pseudo, ClientInterface refClient);
    public void desenregistrer(String pseudo);
    public void diffuser(Message msg);     
}