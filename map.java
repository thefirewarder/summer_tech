import java.util.Random;
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.image.BufferedImage;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
public class map{
    public static void main(String[] args){
        Random random = new Random();
        JFrame frame = new JFrame("Game map");
        frame.setSize(500,500);
        frame.setVisible(true);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        int[][] map = {
            {1,1,1,1,1},
            {1,0,0,0,1},
            {1,0,0,0,1},
            {1,0,0,0,1},
            {1,1,1,1,1},
        };
        String biome;
        int humidity = random.nextInt(100)+1;
        int temperature = random.nextInt(100)+1;
        if(humidity > 70){
            if(temperature > 80){
                biome = "rainforest";
            }
            else if(temperature > 32){
                biome = "swamp";
            }
            else{
                biome = "snowy fields";
            }
        }
        else if(humidity > 30){
            if(temperature > 80){
                biome = "sunny fields";
            }
            else if(temperature > 32){
                biome = "plains";
            }
            else{
                biome = "ice caps";
            }
        }
        else{
            if(temperature > 80){
                biome = "desert";
            }
            else if(temperature > 32){
                biome = "dry forest";
            }
            else{
                biome = "tundra";
            }
        }
    }
    class ImagePanel extends JPanel {
        private BufferedImage img1;
        private BufferedImage img2;

        public ImagePanel(BufferedImage i1, BufferedImage i2) {
             try {
            File rainforestImg = new File("https://art.pixilart.com/6bf06cad21ccc4b.png");
            BufferedImage rainforest= ImageIO.read(rainforestImg);
            this.img1 = i1;
            this.img2 = i2;
             }
             catch (IOException e) {
            System.err.println("Error loading image: " + e.getMessage());
            e.printStackTrace();
        }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g); 
            if (img1 != null) {
                g.drawImage(img1, 0, 0, this); 
            }
            if (img2 != null) {
                g.drawImage(img2, 200, 0, this); 
            }
        }
    }
}
