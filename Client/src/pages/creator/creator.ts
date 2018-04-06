import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { SingletonService } from '../../services/singleton';

@Component({
  selector: 'page-creator',
  templateUrl: 'creator.html'
})
export class CreatorPage {
  
  network: any;
  inputs: any[] = [{'titre' : 'test', 'type': 'number', 'words': ''}];
  outputs: any[] = [];
  constructor(public navCtrl: NavController, private alertCtrl: AlertController, public singleton: SingletonService) {
  	
  }

  newInput(){
    this.inputs.push({'titre' : '', 'type': 'number', 'words': ''});
  }

  newClass(){
    this.outputs.push({'titre' : ''});
  }

  save(){
    let alert = this.alertCtrl.create({
    title: 'Nommer le reseau',
    inputs: [
      {
        name: 'titre',
        placeholder: 'Titre du reseau'
      }
    ],
    buttons: [
      {
        text: 'Annuler',
        role: 'cancel',
        handler: data => {
          console.log('Cancel clicked');
        }
      },
      {
        text: 'Valider',
        handler: data => {
          if (data.titre.length > 0) {
            this.singleton.networks.push({'titre': data.titre, 'inputs': this.inputs, 'outputs': this.outputs})
          } else {
            return false;
          }
        }
      }
    ]
    });
    alert.present();
  }

}
