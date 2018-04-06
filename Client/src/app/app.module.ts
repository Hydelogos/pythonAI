import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';
import { IonicStorageModule } from '@ionic/storage';
import { HTTP } from '@ionic-native/http';

import { SingletonService } from '../services/singleton';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { CreatorPage } from '../pages/creator/creator';
import { SamplePage } from '../pages/sample/sample';

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    CreatorPage,
    SamplePage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    IonicStorageModule.forRoot()
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    CreatorPage,
    SamplePage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    HTTP,
    SingletonService,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
