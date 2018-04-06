import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Storage } from '@ionic/storage';
import { HTTP } from '@ionic-native/http';
import { CreatorPage } from '../creator/creator';
import { SingletonService } from '../../services/singleton';
import { NavParams } from 'ionic-angular';

@Component({
  selector: 'page-sample',
  templateUrl: 'sample.html'
})
export class SamplePage {
  
  index: number;
  network : any;
  samples: any[] = [];
  constructor(public navCtrl: NavController, private storage: Storage, private singleton: SingletonService, private navParams: NavParams) {

  	this.index = navParams.get('index');
    this.network = singleton.networks[i];
    
  }

  newSample(){
    let sample = {values : [], words : []};
    for (var input of this.network.inputs){
      if(input.type)
      sample.values.push(0);
    }
    this.samples.push({})
  }

}
