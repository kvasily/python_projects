#include <iostream>
#include "Playlist.h"
using namespace std;

void PrintMenu(string title) {
    PlaylistNode* headobj = nullptr;
    PlaylistNode* currobj = nullptr;

    while (true) {
        cout << title << " PLAYLIST MENU" << endl;
        cout << "a - Add song" << endl;
        cout << "d - Remove song" << endl;
        cout << "c - Change position of song" << endl;
        cout << "s - Output songs by specific artist" << endl;
        cout << "t - Output total time of playlist (in seconds)" << endl;
        cout << "o - Output full playlist" << endl;
        cout << "q - Quit" << endl;
        cout << "Choose an option:";

        string input;
        cin >> input;
        cin.ignore();

        if (input == "o") {
            if (headobj == nullptr) {
                cout << "Playlist is empty" << endl;
            } else {
                int i = 1;
                cout << title << " - OUTPUT FULL PLAYLIST" << endl;
                currobj = headobj;
                while (currobj != nullptr) {
                    cout << i << "." << endl << "Unique ID: " << currobj->GetID() << endl;
                    cout << "Song Name: " << currobj->GetSongName() << endl;
                    cout << "Artist Name: " << currobj->GetArtistName() << endl;
                    cout << "Song Length (in seconds): " << currobj->GetSongLength() << endl << endl;
                    currobj = currobj->GetNext();
                    i++;
                }
            }
        } else if (input == "a") {
            string ID, sName, aName;
            int sLength;
            cout << "ADD SONG" << endl;
            cout << "Enter song's unique ID:" << endl;
            cin >> ID;
            cin.ignore();
            cout << "Enter song's name:" << endl;
            getline(cin, sName);
            cout << "Enter artist's name:" << endl;
            getline(cin, aName);
            cout << "Enter song's length (in seconds):" << endl;
            cin >> sLength;
            cin.ignore();

            PlaylistNode* newNode = new PlaylistNode(ID, sName, aName, sLength);
            if (!headobj) {
                headobj = newNode;
                currobj = newNode;
            } else {
                currobj->SetNext(newNode);
                currobj = newNode;
            }
        } else if (input == "d") {
string ID; currobj = headobj;
    if (headobj == nullptr) {
      cout << "There are no songs in the playlist." << endl;
    }
    else {
      cout << "REMOVE SONG" << endl << "Enter song's unique ID:" << endl;
      cin.ignore(); cin >> ID; cout << endl;
      if (headobj->GetID() == ID) {
        currobj = currobj->GetNext();
        cout << '"' << headobj->GetSongName() << '" removed' << endl;
        headobj = nullptr;
      }
      else if ((headobj->GetNext() == nullptr) and (headobj->GetID() != ID)) {
        cout << "The unique ID you have entered does not exist";
      }
      else {
        PlaylistNode* tempnext; tempnext = currobj->GetNext();
        while (tempnext->GetID() != ID) {
          if (tempnext->GetNext() == nullptr) {
            cout << "The unique ID you have entered does not exist";
            break;
          }
          currobj = currobj->GetNext(); tempnext = currobj->GetNext();
        }
        if (tempnext->GetID() == ID) {
          currobj = tempnext->GetNext(); //the solution is deceptively simple here!
          cout << '"' << tempnext->GetSongName() << '" removed' << endl;
        }
      }
    }
        } else if (input == "c") {
if (headobj == nullptr) {
      cout << "There are no songs in the playlist." << endl;
    }
    else if (headobj->GetNext() == nullptr) {
      cout << "There is only one song in the playlist." << endl;
    }
    else {
      int cpos, npos, i = 0; currobj = headobj;
      cout << "CHANGE POSITION OF SONG" << endl << "Enter song's current position:" << endl;
      cin.ignore(); cin >> cpos; cout << "Enter new position for song:" << endl; cin >> npos;
      PlaylistNode* tmp1next, tmp2next; tmp1next = currobj->GetNext();
      while (tmp1next->GetNext() != nullptr) {
        if (cpos == i) { // cpos is current position
          break;
        }
        i += 1;
        currobj = currobj->GetNext(); tmp1next = currobj->GetNext();
      } // tmp1next will be the current position, currobj will be the position before tmp1next
      currobj = tmp1next->GetNext(); i = 0; currobj = headobj->GetNext();
      while (currobj->GetNext() != nullptr) {
        if (npos == i) { // npos is new position
          break;
        }
        i += 1;
        headobj = headobj->GetNext(); currobj = headobj->GetNext();
      } // currobj will be the new position, headobj will be the position before currobj
      headobj->InsertAfter(tmp1next);
      if (cpos != i) {
        cout << "You've entered an invalid position. Please try again." << endl;
      }
    }
        } else if (input == "s") {
 if (headobj == nullptr) {
      cout << "There are no songs in the playlist." << endl;
    }
    else {
      string Aname; int i; i = 0; currobj = headobj;
      cout << "OUTPUT SONGS BY SPECIFIC ARTIST" << endl << "Enter artist's name:" << endl;
      cin.ignore(); cin >> Aname; cout << endl << endl;
      while (currobj->GetNext() != nullptr) {
        if (currobj->GetArtistName() == Aname) {
          cout << i << "." << endl << "Unique ID: " << currobj->GetID() << endl << "Song Name: ";
          cout << currobj->GetSongName() << endl << "Artist Name: " << Aname << endl;
          cout << "Song Length (in seconds): " << currobj->GetSongLength() << endl << endl;
        } // could not figure out what the exception handling would be if an invalid artist name was input
        currobj = currobj->GetNext(); i += 1;
      }
    }
        } else if (input == "t") {
            PlaylistNode* tempNode = headobj;
            int totalTime = 0;
            while (tempNode) {
                totalTime += tempNode->GetSongLength();
                tempNode = tempNode->GetNext();
            }
            cout << "OUTPUT TOTAL TIME OF PLAYLIST (IN SECONDS)" << endl;
            cout << "Total time: " << totalTime << " seconds" << endl;
        } else if (input == "q") {
            // Cleanup memory
            while (headobj) {
                PlaylistNode* tmp = headobj;
                headobj = headobj->GetNext();
                delete tmp;
            }
            break;
        }
    }
}

int main() {
    string playlistTitle;
    cout << "Enter playlist's title:" << endl;
    getline(cin, playlistTitle);
    PrintMenu(playlistTitle);
    return 0;
}
