terraform { 
  cloud { 
    
    organization = "Cloud-technologies-group" 

    workspaces { 
      name = "devop-qr" 
    } 
  } 
}