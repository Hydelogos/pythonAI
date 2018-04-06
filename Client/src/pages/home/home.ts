import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Storage } from '@ionic/storage';
import { HTTP } from '@ionic-native/http';
import { CreatorPage } from '../creator/creator';
import { SamplePage } from '../sample/sample';
import { SingletonService } from '../../services/singleton';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  
  needServer : boolean;
  servIp : string;
  servPort: string;
  constructor(public navCtrl: NavController, private storage: Storage, private http: HTTP, private singleton: SingletonService) {
  	this.needServer = false;
  	this.servIp = "127.0.0.1";
  	this.servPort = "80";
  	var home = this;
  	storage.ready().then((stoready) => {
  		storage.get("servIp").then((val)=>{
  		 storage.get("servPort").then((val2) =>{
  		 	if(val && val2){
  		 		this.http.get('http://' + this.servIp + ':' + this.servPort, {}, {}).then(data => {
  		 			home.needServer = false;
  		 		}).catch(error => {
  		 			console.log(error)
  		 		});
  		 	}
  		 })
  		})
  	});
  }

  servTest(){
  	console.log(this.servIp);
  	console.log(this.servPort);
  	this.storage.set("servIp", this.servIp);
  	this.storage.set("servPort", this.servPort);
  	var home = this;
  	this.http.get('http://' + this.servIp + ':' + this.servPort, {}, {}).then(data => {
  		home.needServer = false;
  	}).catch(error => {
  		console.log(error)
  	});
  }

  addNetwork(){
    this.navCtrl.push(CreatorPage);
  }

  addSamples(i : number){
    this.navCtrl.push(SamplePage, {'index': i});
  }

}
